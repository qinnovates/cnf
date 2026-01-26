/**
 * Title Scene - Apple-quality logo reveal
 * Features: Blur-in text, spring physics, liquid glass effects
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, Img, staticFile, interpolate } from 'remotion';
import { NeuralFlow, NeuralFlowBackground } from '../components/NeuralFlow';
import { FloatingParticles } from '../components/Particles';
import { BlurInText, GradualSpacing } from '../components/TextAnimations';
import { colors } from '../data/oni-theme';

export const TitleScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Phase 1: Logo reveal with spring
  const logoScale = spring({
    frame,
    fps,
    config: { damping: 15, stiffness: 60 },
  });

  const logoOpacity = spring({
    frame,
    fps,
    config: { damping: 80, stiffness: 150 },
  });

  // Glow pulse - smooth and subtle
  const glowPhase = Math.sin(frame * 0.06);
  const glowIntensity = interpolate(glowPhase, [-1, 1], [0.4, 0.9]);

  // Phase 2: Text reveals
  const textRevealDelay = 20;
  const taglineDelay = 35;
  const descriptorDelay = 50;

  // Neural flow activation timing
  const flowState = frame > 40 ? 'reactive' : 'resting';

  // Outer ring pulse effect
  const ringProgress = spring({
    frame: frame - 10,
    fps,
    config: { damping: 100, stiffness: 50 },
  });

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at center, ${colors.primary.main}18 0%, ${colors.primary.dark} 70%)`,
      }}
    >
      {/* Subtle particle field */}
      <FloatingParticles
        count={80}
        color={colors.primary.accent}
        speed={0.2}
        minSize={1}
        maxSize={4}
      />

      {/* Neural flow background - very subtle */}
      <NeuralFlowBackground numLines={3} opacity={0.1} />

      {/* Expanding ring behind logo */}
      {[0, 1, 2].map((i) => {
        const ringSize = interpolate(
          Math.max(0, ringProgress),
          [0, 1],
          [200, 600 + i * 200]
        );
        const ringOpacity = interpolate(
          Math.max(0, ringProgress),
          [0, 0.3, 1],
          [0, 0.15, 0.03 - i * 0.01]
        );

        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              top: '50%',
              left: '50%',
              width: ringSize,
              height: ringSize,
              borderRadius: '50%',
              border: `1px solid ${colors.primary.accent}`,
              transform: 'translate(-50%, -50%)',
              opacity: Math.max(0, ringOpacity),
            }}
          />
        );
      })}

      {/* Radial glow behind logo - liquid glass effect */}
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width: 900,
          height: 600,
          borderRadius: '50%',
          background: `radial-gradient(ellipse, ${colors.primary.accent}${Math.round(glowIntensity * 25).toString(16).padStart(2, '0')} 0%, transparent 55%)`,
          filter: 'blur(60px)',
          opacity: logoOpacity,
        }}
      />

      {/* Main content container */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          height: '100%',
          gap: 30,
        }}
      >
        {/* ONI Banner Logo with smooth reveal */}
        <div
          style={{
            transform: `scale(${interpolate(Math.max(0, logoScale), [0, 1], [0.85, 1])})`,
            opacity: Math.max(0, logoOpacity),
            filter: `
              drop-shadow(0 0 ${20 * glowIntensity}px ${colors.primary.accent}55)
              drop-shadow(0 0 ${60 * glowIntensity}px ${colors.primary.accent}22)
            `,
          }}
        >
          <Img
            src={staticFile('assets/ONI_Banner_Logo.png')}
            style={{
              width: 700,
              objectFit: 'contain',
            }}
          />
        </div>

        {/* Neural Flow under logo - ElevenLabs inspired */}
        <div
          style={{
            marginTop: -10,
            opacity: interpolate(frame, [25, 40], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
          }}
        >
          <NeuralFlow
            state={flowState}
            width={450}
            height={50}
            intensity={0.7}
          />
        </div>

        {/* Tagline with blur-in effect */}
        <div style={{ marginTop: 20 }}>
          <BlurInText
            text="The OSI of Mind"
            delay={taglineDelay}
            fontSize={36}
            color={colors.primary.accent}
            fontWeight={300}
          />
        </div>

        {/* Descriptor with gradual spacing */}
        <GradualSpacing
          text="Neural Security Framework"
          delay={descriptorDelay}
          fontSize={16}
          color={colors.text.muted}
          fontWeight={400}
        />
      </div>

      {/* Corner accents - more refined */}
      {[
        { top: 50, left: 50, borderTop: true, borderLeft: true },
        { top: 50, right: 50, borderTop: true, borderRight: true },
        { bottom: 50, left: 50, borderBottom: true, borderLeft: true },
        { bottom: 50, right: 50, borderBottom: true, borderRight: true },
      ].map((corner, i) => {
        const cornerProgress = spring({
          frame: frame - 60 - i * 5,
          fps,
          config: { damping: 30, stiffness: 100 },
        });

        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              top: corner.top,
              left: corner.left,
              right: corner.right,
              bottom: corner.bottom,
              width: 80,
              height: 80,
              borderTop: corner.borderTop
                ? `1px solid ${colors.primary.accent}33`
                : 'none',
              borderBottom: corner.borderBottom
                ? `1px solid ${colors.primary.accent}33`
                : 'none',
              borderLeft: corner.borderLeft
                ? `1px solid ${colors.primary.accent}33`
                : 'none',
              borderRight: corner.borderRight
                ? `1px solid ${colors.primary.accent}33`
                : 'none',
              opacity: Math.max(0, cornerProgress),
              transform: `scale(${interpolate(
                Math.max(0, cornerProgress),
                [0, 1],
                [0.8, 1]
              )})`,
            }}
          />
        );
      })}

      {/* Bottom gradient fade */}
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: 150,
          background: `linear-gradient(transparent, ${colors.primary.dark}88)`,
          pointerEvents: 'none',
        }}
      />
    </AbsoluteFill>
  );
};
