#!/usr/bin/env python3
"""
LearnViz - Automated Learning Visualization Pipeline

Transform concept descriptions into educational visualizations.

Usage:
    python learnviz.py "Explain binary search"
    python learnviz.py "Pythagorean theorem proof" --format gif
    python learnviz.py "Bubble sort algorithm" --engine manim --render
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from analyzer import analyze, VisualizationPlan, Engine
from generators.manim_gen import generate_manim_code, TEMPLATES
from generators.narration import ScriptGenerator, TTSGenerator, NarrationScript


# Output directory
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def print_banner():
    """Print the LearnViz banner."""
    banner = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║   ██╗     ███████╗ █████╗ ██████╗ ███╗   ██╗██╗   ██╗██╗███████╗║
    ║   ██║     ██╔════╝██╔══██╗██╔══██╗████╗  ██║██║   ██║██║╚══███╔╝║
    ║   ██║     █████╗  ███████║██████╔╝██╔██╗ ██║██║   ██║██║  ███╔╝ ║
    ║   ██║     ██╔══╝  ██╔══██║██╔══██╗██║╚██╗██║╚██╗ ██╔╝██║ ███╔╝  ║
    ║   ███████╗███████╗██║  ██║██║  ██║██║ ╚████║ ╚████╔╝ ██║███████╗║
    ║   ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝╚══════╝║
    ║                                                               ║
    ║   Concept → Code → Video                                      ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def generate_filename(concept: str, extension: str = "py") -> str:
    """Generate a filename from the concept description."""
    # Clean the concept for filename
    clean = concept.lower()
    clean = "".join(c if c.isalnum() or c == " " else "" for c in clean)
    clean = "_".join(clean.split()[:5])  # First 5 words
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{clean}_{timestamp}.{extension}"


def check_dependencies():
    """Check if required dependencies are installed."""
    deps = {
        "manim": "pip install manim",
        "remotion": "npm install -g @remotion/cli"
    }

    missing = []

    # Check Manim
    try:
        subprocess.run(
            ["python", "-c", "import manim"],
            capture_output=True,
            check=True
        )
    except subprocess.CalledProcessError:
        missing.append(("manim", deps["manim"]))

    if missing:
        print("\nMissing dependencies:")
        for dep, install_cmd in missing:
            print(f"  - {dep}: {install_cmd}")
        print()

    return len(missing) == 0


def render_manim(code_path: str, output_format: str = "mp4", quality: str = "l") -> str:
    """
    Render Manim code to video.

    Args:
        code_path: Path to the Python file
        output_format: 'mp4' or 'gif'
        quality: 'l' (low), 'm' (medium), 'h' (high), 'k' (4k)

    Returns:
        Path to rendered output
    """
    # Extract scene class name
    with open(code_path, "r") as f:
        content = f.read()

    # Find class name (assumes single Scene class)
    import re
    match = re.search(r"class (\w+)\(Scene\)", content)
    if not match:
        raise ValueError("No Scene class found in generated code")

    scene_name = match.group(1)

    # Determine output format flag
    format_flag = "--format gif" if output_format == "gif" else ""

    # Build command
    cmd = f"manim -pq{quality} {format_flag} {code_path} {scene_name}"

    print(f"\nRendering with command: {cmd}")
    print("-" * 60)

    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Render failed:\n{result.stderr}")
        return None

    print(result.stdout)

    # Find output file
    media_dir = Path("media/videos") / Path(code_path).stem / f"{quality}80p15"
    if output_format == "gif":
        media_dir = Path("media/videos") / Path(code_path).stem / "images"

    if media_dir.exists():
        files = list(media_dir.glob(f"*.{output_format}"))
        if files:
            return str(files[0])

    return None


def interactive_mode(plan: VisualizationPlan):
    """Interactive mode for refining the visualization plan."""
    print("\n" + "=" * 60)
    print("INTERACTIVE MODE")
    print("=" * 60)

    print("\nCurrent plan:")
    print(f"  Type: {plan.concept_type.value}")
    print(f"  Engine: {plan.engine.value}")
    print(f"  Complexity: {plan.complexity}")
    print(f"  Scenes: {len(plan.scenes)}")
    print(f"  Template: {plan.template or 'None'}")

    print("\nOptions:")
    print("  [1] Change engine")
    print("  [2] Change complexity")
    print("  [3] Select template")
    print("  [4] Edit scenes")
    print("  [5] Continue with current plan")
    print("  [q] Quit")

    while True:
        choice = input("\nChoice: ").strip()

        if choice == "1":
            print("\nAvailable engines:")
            for e in Engine:
                print(f"  - {e.value}")
            new_engine = input("Engine: ").strip()
            try:
                plan.engine = Engine(new_engine)
                print(f"Engine set to: {plan.engine.value}")
            except ValueError:
                print("Invalid engine")

        elif choice == "2":
            print("\nComplexity options: simple, moderate, complex")
            new_complexity = input("Complexity: ").strip()
            if new_complexity in ["simple", "moderate", "complex"]:
                plan.complexity = new_complexity
                print(f"Complexity set to: {plan.complexity}")
            else:
                print("Invalid complexity")

        elif choice == "3":
            print("\nAvailable templates:")
            for name, template in TEMPLATES.items():
                print(f"  - {name}: {template.description}")
            new_template = input("Template (or 'none'): ").strip()
            if new_template == "none":
                plan.template = None
            elif new_template in TEMPLATES:
                plan.template = new_template
            print(f"Template set to: {plan.template}")

        elif choice == "4":
            print("\nScenes:")
            for s in plan.scenes:
                print(f"  [{s.id}] {s.name}: {s.description}")
            print("\n(Scene editing not yet implemented)")

        elif choice == "5":
            break

        elif choice.lower() == "q":
            sys.exit(0)

    return plan


def main():
    parser = argparse.ArgumentParser(
        description="LearnViz - Automated Learning Visualization Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python learnviz.py "Explain binary search"
  python learnviz.py "Bubble sort" --template sort_visual
  python learnviz.py "Pythagorean theorem" --render --format gif
  python learnviz.py "Tree traversal" --interactive
        """
    )

    parser.add_argument(
        "concept",
        help="Concept description to visualize"
    )
    parser.add_argument(
        "--engine",
        choices=["manim", "remotion", "d3", "mermaid"],
        help="Force specific rendering engine"
    )
    parser.add_argument(
        "--template",
        help="Use specific template"
    )
    parser.add_argument(
        "--format",
        choices=["mp4", "gif"],
        default="mp4",
        help="Output format (default: mp4)"
    )
    parser.add_argument(
        "--quality",
        choices=["l", "m", "h", "k"],
        default="l",
        help="Render quality: l=low, m=medium, h=high, k=4k (default: l)"
    )
    parser.add_argument(
        "--render",
        action="store_true",
        help="Render the visualization after generating code"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Interactive mode to refine the plan"
    )
    parser.add_argument(
        "--output",
        help="Output filename (without extension)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output plan as JSON only"
    )
    parser.add_argument(
        "--list-templates",
        action="store_true",
        help="List available templates"
    )
    parser.add_argument(
        "--params",
        help="JSON parameters for template (e.g., '{\"array\": [1,2,3]}')"
    )
    parser.add_argument(
        "--narration",
        action="store_true",
        help="Generate narration script for the visualization"
    )
    parser.add_argument(
        "--tts",
        choices=["gtts", "pyttsx3", "edge-tts"],
        help="Generate text-to-speech audio (requires --narration)"
    )
    parser.add_argument(
        "--tts-only",
        action="store_true",
        help="Only generate narration/TTS, skip video generation"
    )

    args = parser.parse_args()

    # List templates
    if args.list_templates:
        print("\nAvailable Templates:")
        print("-" * 60)
        for name, template in TEMPLATES.items():
            print(f"  {name:20} - {template.description}")
        print()
        return

    print_banner()

    # Analyze concept
    print(f"\nAnalyzing: \"{args.concept}\"")
    print("-" * 60)

    plan = analyze(args.concept)

    # Override engine if specified
    if args.engine:
        plan.engine = Engine(args.engine)

    # Override template if specified
    if args.template:
        plan.template = args.template

    # JSON output only
    if args.json:
        print(plan.to_json())
        return

    # Print analysis
    print(f"\n{'=' * 60}")
    print("ANALYSIS RESULT")
    print(f"{'=' * 60}")
    print(f"  Title:      {plan.title}")
    print(f"  Type:       {plan.concept_type.value}")
    print(f"  Engine:     {plan.engine.value}")
    print(f"  Complexity: {plan.complexity}")
    print(f"  Scenes:     {len(plan.scenes)}")
    print(f"  Duration:   ~{plan.total_duration}s")
    print(f"  Template:   {plan.template or 'None (generic)'}")

    # Interactive mode
    if args.interactive:
        plan = interactive_mode(plan)

    # Skip code generation if --tts-only
    output_path = None
    if args.tts_only:
        print(f"\n{'=' * 60}")
        print("SKIPPING CODE GENERATION (--tts-only)")
        print(f"{'=' * 60}")
    else:
        # Generate code
        print(f"\n{'=' * 60}")
        print("GENERATING CODE")
        print(f"{'=' * 60}")

    # Parse template parameters
    params = {}
    if args.params:
        try:
            params = json.loads(args.params)
        except json.JSONDecodeError:
            print(f"Warning: Could not parse params JSON: {args.params}")

    # Currently only Manim is fully implemented
    if plan.engine == Engine.MANIM and not args.tts_only:
        code = generate_manim_code(
            plan.to_dict(),
            template_name=plan.template,
            params=params
        )

        # Save code
        filename = args.output or generate_filename(args.concept, "py")
        output_path = OUTPUT_DIR / filename

        with open(output_path, "w") as f:
            f.write(code)

        print(f"\nGenerated: {output_path}")

        # Render if requested
        if args.render:
            print(f"\n{'=' * 60}")
            print("RENDERING")
            print(f"{'=' * 60}")

            if not check_dependencies():
                print("Install missing dependencies and try again.")
                return

            result = render_manim(
                str(output_path),
                output_format=args.format,
                quality=args.quality
            )

            if result:
                print(f"\nRendered: {result}")
            else:
                print("\nRender failed. Check the generated code.")

    elif not args.tts_only:
        print(f"\nEngine '{plan.engine.value}' code generation not yet implemented.")
        print("Currently supported: manim")
        print("\nPlan saved as JSON:")
        json_path = OUTPUT_DIR / generate_filename(args.concept, "json")
        with open(json_path, "w") as f:
            f.write(plan.to_json())
        print(f"  {json_path}")

    # Generate narration if requested
    if args.narration or args.tts:
        print(f"\n{'=' * 60}")
        print("GENERATING NARRATION")
        print(f"{'=' * 60}")

        # Map template to narration script
        narration_type = plan.template
        if narration_type in ["neuron_structure"]:
            narration_type = "action_potential"

        try:
            script = ScriptGenerator.generate_script(narration_type or "general")
            print(f"\nNarration script generated: {script.title}")
            print(f"Total duration: {script.total_duration:.1f}s")
            print(f"Segments: {len(script.segments)}")

            # Save script to file
            script_filename = generate_filename(args.concept, "json").replace(".json", "_narration.json")
            script_path = OUTPUT_DIR / script_filename
            with open(script_path, "w") as f:
                f.write(script.to_json())
            print(f"\nScript saved: {script_path}")

            # Also save as plain text
            text_filename = script_filename.replace(".json", ".txt")
            text_path = OUTPUT_DIR / text_filename
            with open(text_path, "w") as f:
                f.write(f"# {script.title}\n")
                f.write(f"# Total duration: {script.total_duration:.1f}s\n\n")
                for seg in script.segments:
                    f.write(f"## {seg.id} ({seg.duration}s)\n")
                    f.write(f"{seg.text}\n\n")
            print(f"Text script saved: {text_path}")

            # Generate TTS if requested
            if args.tts:
                print(f"\nGenerating TTS audio with {args.tts}...")
                tts = TTSGenerator(engine=args.tts, output_dir=str(OUTPUT_DIR))
                audio_filename = generate_filename(args.concept, "mp3").replace(".mp3", "_narration.mp3")
                audio_path = tts.generate(script, filename=audio_filename)
                if audio_path:
                    print(f"Audio saved: {audio_path}")
                else:
                    print("TTS generation failed. Check that the TTS engine is installed.")

        except Exception as e:
            print(f"Narration generation error: {e}")
            print("Note: Narration templates are available for: action_potential, synapse")

    print(f"\n{'=' * 60}")
    print("DONE")
    print(f"{'=' * 60}")

    # Print next steps
    print("\nNext steps:")
    if not args.render and plan.engine == Engine.MANIM and not args.tts_only:
        print(f"  1. Review generated code: {output_path}")
        print(f"  2. Render: python learnviz.py \"{args.concept}\" --render")
    if not args.narration:
        print(f"  3. Add narration: python learnviz.py \"{args.concept}\" --narration --tts gtts")
    print("  4. Edit code to customize the visualization")
    print("  5. Re-render with higher quality: --quality h")


if __name__ == "__main__":
    main()
