import { AbsoluteFill, Sequence } from "remotion";
import { colors, sceneTimestamps } from "./data/oni-theme";

// Scene components
import { ColdOpenScene } from "./scenes/ColdOpenScene";
import { TitleScene } from "./scenes/TitleScene";
import { ProblemScene } from "./scenes/ProblemScene";
import { LayersScene } from "./scenes/ONILayersAnimation";
import { CoherenceScene } from "./scenes/CoherenceScene";
import { TARAScene } from "./scenes/TARAScene";
import { AcademicScene } from "./scenes/AcademicScene";
import { CTAScene } from "./scenes/CTAScene";
import { CreditsScene } from "./scenes/CreditsScene";

// Persistent components
import { Watermark } from "./components/Watermark";

export const ONIDemoVideo: React.FC = () => {
  const { coldOpen, title, problem, layers, coherence, tara, academic, cta, credits } = sceneTimestamps;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: colors.primary.dark,
        fontFamily: "'Inter', sans-serif",
      }}
    >
      {/* Background audio - add when files are available */}
      {/* <Audio src={staticFile("audio/voiceover.mp3")} /> */}
      {/* <Audio src={staticFile("audio/background.mp3")} volume={0.3} /> */}

      {/* Scene 0: Cold Open (0:00-0:08) */}
      <Sequence from={coldOpen.start} durationInFrames={coldOpen.end - coldOpen.start}>
        <ColdOpenScene />
      </Sequence>

      {/* Scene 1: Title (0:08-0:15) */}
      <Sequence from={title.start} durationInFrames={title.end - title.start}>
        <TitleScene />
      </Sequence>

      {/* Scene 2: Problem Statement (0:15-0:40) */}
      <Sequence from={problem.start} durationInFrames={problem.end - problem.start}>
        <ProblemScene />
      </Sequence>

      {/* Scene 3: 14-Layer Model (0:40-1:20) */}
      <Sequence from={layers.start} durationInFrames={layers.end - layers.start}>
        <LayersScene />
      </Sequence>

      {/* Scene 4: Coherence Metric (1:20-1:50) */}
      <Sequence from={coherence.start} durationInFrames={coherence.end - coherence.start}>
        <CoherenceScene />
      </Sequence>

      {/* Scene 5: TARA Stack (1:50-2:25) */}
      <Sequence from={tara.start} durationInFrames={tara.end - tara.start}>
        <TARAScene />
      </Sequence>

      {/* Scene 6: Academic Foundation (2:25-2:50) */}
      <Sequence from={academic.start} durationInFrames={academic.end - academic.start}>
        <AcademicScene />
      </Sequence>

      {/* Scene 7: Call to Action (2:50-3:15) */}
      <Sequence from={cta.start} durationInFrames={cta.end - cta.start}>
        <CTAScene />
      </Sequence>

      {/* Scene 8: Credits (3:15-3:30) */}
      <Sequence from={credits.start} durationInFrames={credits.end - credits.start}>
        <CreditsScene />
      </Sequence>

      {/* Persistent watermark - © 2026 Kevin Qi • ONI Framework™ */}
      <Watermark position="bottom-right" opacity={0.6} fadeInDelay={60} />
    </AbsoluteFill>
  );
};
