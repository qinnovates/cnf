/**
 * ONI Framework Demo Video Script
 * ~400 words, 3:30 runtime
 *
 * For ElevenLabs generation, use voice: "Adam" (authoritative) or "Rachel" (professional)
 * Request word-level timestamps for precise sync
 */

export interface ScriptLine {
  text: string;
  startFrame: number;
  endFrame: number;
  scene: string;
}

export const script: ScriptLine[] = [
  // Scene 0: Cold Open (0:00-0:08)
  {
    scene: 'coldOpen',
    text: "Brain-computer interfaces are no longer science fiction.",
    startFrame: 0,
    endFrame: 120,
  },
  {
    scene: 'coldOpen',
    text: "They're in operating rooms. They're in research labs. They're coming to consumers.",
    startFrame: 120,
    endFrame: 240,
  },

  // Scene 1: Title (0:08-0:15)
  {
    scene: 'title',
    text: "But who's protecting the most sensitive data in existence?",
    startFrame: 240,
    endFrame: 360,
  },
  {
    scene: 'title',
    text: "Your thoughts.",
    startFrame: 360,
    endFrame: 450,
  },

  // Scene 2: Problem (0:15-0:40)
  {
    scene: 'problem',
    text: "Today's brain-computer interfaces lack standardized security frameworks.",
    startFrame: 450,
    endFrame: 570,
  },
  {
    scene: 'problem',
    text: "There's no OSI model for neural interfaces.",
    startFrame: 570,
    endFrame: 690,
  },
  {
    scene: 'problem',
    text: "No common language between neuroscientists, engineers, and security researchers.",
    startFrame: 690,
    endFrame: 870,
  },
  {
    scene: 'problem',
    text: "Until now.",
    startFrame: 870,
    endFrame: 960,
  },
  {
    scene: 'problem',
    text: "Introducing ONI—the Open Neurosecurity Interoperability.",
    startFrame: 960,
    endFrame: 1140,
  },
  {
    scene: 'problem',
    text: "A universal framework. Secure by design. Ready for the biodigital future.",
    startFrame: 1140,
    endFrame: 1380,
  },

  // Scene 3: 14-Layer Model (0:46-1:26)
  {
    scene: 'layers',
    text: "ONI defines fourteen layers spanning silicon to synapse.",
    startFrame: 1380,
    endFrame: 1530,
  },
  {
    scene: 'layers',
    text: "Layers one through seven mirror the classical OSI model—physical signals, protocols, transport, and application interfaces.",
    startFrame: 1530,
    endFrame: 1830,
  },
  {
    scene: 'layers',
    text: "But here's where ONI goes further.",
    startFrame: 1830,
    endFrame: 1950,
  },
  {
    scene: 'layers',
    text: "Layer eight is the Neural Gateway—the critical bridge where silicon meets synapse.",
    startFrame: 1950,
    endFrame: 2190,
  },
  {
    scene: 'layers',
    text: "This is where traditional security ends and neurosecurity begins.",
    startFrame: 2190,
    endFrame: 2370,
  },
  {
    scene: 'layers',
    text: "Layers nine through fourteen map the biological stack—from ion channels to spike trains, neural populations, circuit dynamics, cognitive function, and ultimately, identity.",
    startFrame: 2370,
    endFrame: 2580,
  },

  // Scene 4: Coherence Metric (1:26-2:06)
  {
    scene: 'coherence',
    text: "But how do you measure neural security?",
    startFrame: 2580,
    endFrame: 2700,
  },
  {
    scene: 'coherence',
    text: "ONI introduces the Coherence Score—a unified metric combining phase variance, timing precision, and frequency stability.",
    startFrame: 2700,
    endFrame: 2940,
  },
  {
    scene: 'coherence',
    text: "When coherence drops below threshold, automated defense mechanisms activate.",
    startFrame: 2940,
    endFrame: 3120,
  },
  {
    scene: 'coherence',
    text: "Whether it's MRI interference, electromagnetic disruption, or a malicious injection attack—the system responds instantly.",
    startFrame: 3120,
    endFrame: 3360,
  },
  {
    scene: 'coherence',
    text: "And the Scale-Frequency Invariant ensures neural patterns maintain constant relationships across all scales.",
    startFrame: 3360,
    endFrame: 3600,
  },
  {
    scene: 'coherence',
    text: "As scale increases, frequency decreases proportionally. The product remains invariant—a fingerprint of healthy neural activity.",
    startFrame: 3600,
    endFrame: 3840,
  },

  // Scene 5: TARA Platform (2:06-2:36)
  {
    scene: 'tara',
    text: "For security professionals, there's TARA—the Telemetry Analysis and Response Automation platform.",
    startFrame: 3840,
    endFrame: 4080,
  },
  {
    scene: 'tara',
    text: "Real-time brain topology visualization.",
    startFrame: 4080,
    endFrame: 4230,
  },
  {
    scene: 'tara',
    text: "Attack simulation across all fourteen layers.",
    startFrame: 4230,
    endFrame: 4410,
  },
  {
    scene: 'tara',
    text: "Neural Signal Assurance Monitoring that flags anomalies before they become breaches.",
    startFrame: 4410,
    endFrame: 4680,
  },

  // Scene 6: Academic Foundation (2:36-3:01)
  {
    scene: 'academic',
    text: "ONI isn't built in a vacuum.",
    startFrame: 4680,
    endFrame: 4800,
  },
  {
    scene: 'academic',
    text: "It extends the threat models of Kohno and colleagues at the University of Washington.",
    startFrame: 4800,
    endFrame: 5040,
  },
  {
    scene: 'academic',
    text: "It incorporates neurosecurity research from Columbia, Yale, and the Graz BCI Lab.",
    startFrame: 5040,
    endFrame: 5310,
  },
  {
    scene: 'academic',
    text: "Every claim is cited. Every formula is documented.",
    startFrame: 5310,
    endFrame: 5460,
  },
  {
    scene: 'academic',
    text: "Built for researchers, developers, regulators, security teams...",
    startFrame: 5460,
    endFrame: 5640,
  },
  {
    scene: 'academic',
    // NOTE: This line should have slow pan-in animation with WHITE TEXT for dramatic emphasis
    text: "...and you.",
    startFrame: 5640,
    endFrame: 5880, // Extended for dramatic effect
  },

  // Scene 7: Call to Action (3:01-3:21)
  {
    scene: 'cta',
    text: "Ready to secure the neural frontier?",
    startFrame: 5880,
    endFrame: 6030,
  },
  {
    scene: 'cta',
    text: "Install ONI with a single command.",
    startFrame: 6030,
    endFrame: 6180,
  },
  {
    scene: 'cta',
    text: "pip install oni-framework, oni-tara, or oni-academy",
    startFrame: 6180,
    endFrame: 6360,
  },
  {
    scene: 'cta',
    text: "Join us in building the security standards for brain-computer interfaces.",
    startFrame: 6360,
    endFrame: 6570,
  },

  // Scene 8: Credits (3:21-3:53) - Powerful closing with dynamic waves
  {
    scene: 'credits',
    text: "Our mind.",
    startFrame: 6570,
    endFrame: 6660,
  },
  {
    scene: 'credits',
    text: "Our future.",
    startFrame: 6660,
    endFrame: 6750,
  },
  {
    scene: 'credits',
    text: "Our rules.",
    startFrame: 6750,
    endFrame: 6840,
  },
  {
    scene: 'credits',
    text: "Because life's most important connections deserve the most thought.",
    startFrame: 6840,
    endFrame: 7050,
  },
  {
    scene: 'credits',
    text: "Welcome to the OSI of Mind.",
    startFrame: 7050,
    endFrame: 7290,
  },
];

// Full script as single text for voiceover generation
export const fullScript = script.map(line => line.text).join(' ');

// Word count: ~440 words
// Estimated read time at 110 WPM: ~4:03 (fits 4:03 with natural pacing)
// Final frame: 7290 = 4:03 at 30fps
//
// ANIMATION NOTES:
// - Scene 2 (Problem): NEW selling points phase after "ONI Framework" intro
//   - Universal, Secure by Design, Biodigital Ready - staggered reveal
// - Scene 4 (Coherence): Show threshold trigger → defense mechanism activation
//   - Visual: Gauge drops below threshold → shield/alert animation
//   - Examples: MRI interference, electromagnetic disruption, injection attacks
// - Scene 4 (Scale-Frequency): Animated visualization of f × S ≈ k
//   - Scale bar grows (10→1000), Frequency shrinks (100→1 Hz), k stays ~1000
// - Scene 6 ("...and you"): SLOW PAN-IN with WHITE TEXT and glow for emphasis
// - Scene 7 (CTA): Cycling pip install animation (framework → tara → academy)
// - Scene 8 (Credits): Dynamic circular wave animation on "Welcome to" finale
// - Cold Open: Wave grid fades in 5 seconds before transition for continuity
