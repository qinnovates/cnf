/**
 * Credits Scene - Final logo and credits
 * Features: Smooth fade, pulsing logo, elegant typography
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, Img, staticFile, interpolate } from 'remotion';
import { FloatingParticles } from '../components/Particles';
import { NeuralFlow } from '../components/NeuralFlow';
import { BlurInText, GradualSpacing } from '../components/TextAnimations';
import { colors } from '../data/oni-theme';

export const CreditsScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Fade in
  const fadeIn = spring({
    frame,
    fps,
    config: { damping: 40, stiffness: 60 },
  });

  // Logo pulse - very subtle
  const logoPulse = interpolate(
    Math.sin(frame * 0.06),
    [-1, 1],
    [0.98, 1.02]
  );

  // Glow intensity
  const glowIntensity = interpolate(
    Math.sin(frame * 0.05),
    [-1, 1],
    [0.3, 0.6]
  );

  return (
    <AbsoluteFill
      style={{
        background: colors.gradients.background,
      }}
    >
      {/* Very subtle particles */}
      <FloatingParticles
        count={30}
        color={colors.primary.accent}
        speed={0.1}
        minSize={1}
        maxSize={2}
      />

      {/* Content */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          height: '100%',
          gap: 32,
          opacity: Math.max(0, fadeIn),
        }}
      >
        {/* Expanding rings behind logo */}
        {[0, 1, 2].map((i) => {
          const ringDelay = i * 20;
          const ringProgress = interpolate(
            frame - ringDelay,
            [0, 60],
            [0, 1],
            { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
          );

          return (
            <div
              key={i}
              style={{
                position: 'absolute',
                top: '50%',
                left: '50%',
                width: interpolate(ringProgress, [0, 1], [100, 400 + i * 100]),
                height: interpolate(ringProgress, [0, 1], [100, 400 + i * 100]),
                borderRadius: '50%',
                border: `1px solid ${colors.primary.accent}`,
                transform: 'translate(-50%, -50%)',
                opacity: interpolate(ringProgress, [0, 0.3, 1], [0, 0.2, 0.03]),
              }}
            />
          );
        })}

        {/* ONI Logo with glow */}
        <div
          style={{
            transform: `scale(${logoPulse})`,
            filter: `drop-shadow(0 0 ${30 * glowIntensity}px ${colors.primary.accent}44)`,
          }}
        >
          <Img
            src={staticFile('assets/ONI_Logo.png')}
            style={{
              width: 180,
              objectFit: 'contain',
            }}
          />
        </div>

        {/* Title with blur-in */}
        <BlurInText
          text="Open Neural Interface Framework"
          delay={15}
          fontSize={44}
          fontWeight={600}
          gradient={true}
        />

        {/* Tagline with gradual spacing */}
        <GradualSpacing
          text="The OSI of Mind"
          delay={35}
          fontSize={18}
          color={colors.primary.accent}
          fontWeight={400}
        />

        {/* Divider line */}
        <div
          style={{
            width: interpolate(frame - 50, [0, 40], [0, 150], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
            height: 1,
            background: `linear-gradient(90deg, transparent, ${colors.primary.accent}44, transparent)`,
            margin: '16px 0',
          }}
        />

        {/* Credits info */}
        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: 14,
            opacity: interpolate(frame - 70, [0, 30], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
          }}
        >
          <div
            style={{
              fontSize: 18,
              color: colors.text.secondary,
            }}
          >
            Created by{' '}
            <span style={{ color: colors.text.primary, fontWeight: 600 }}>
              Kevin Qi
            </span>
          </div>

          <div
            style={{
              fontSize: 14,
              color: colors.text.muted,
            }}
          >
            Apache 2.0 License
          </div>
        </div>

        {/* Built with Claude badge */}
        <div
          style={{
            marginTop: 30,
            padding: '12px 24px',
            background: 'rgba(255, 255, 255, 0.03)',
            backdropFilter: 'blur(10px)',
            borderRadius: 10,
            border: '1px solid rgba(255,255,255,0.06)',
            display: 'flex',
            alignItems: 'center',
            gap: 10,
            opacity: interpolate(frame - 100, [0, 30], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
          }}
        >
          <span style={{ fontSize: 14, color: colors.text.muted }}>
            Built with
          </span>
          <span
            style={{
              fontSize: 14,
              color: colors.primary.accent,
              fontWeight: 600,
            }}
          >
            Claude Code
          </span>
        </div>

        {/* Neural flow at bottom */}
        <div
          style={{
            position: 'absolute',
            bottom: 100,
            opacity: 0.3,
          }}
        >
          <NeuralFlow
            state="resting"
            width={400}
            height={35}
            intensity={0.3}
          />
        </div>

        {/* Year */}
        <div
          style={{
            position: 'absolute',
            bottom: 40,
            fontSize: 14,
            color: colors.text.muted,
            opacity: 0.6,
          }}
        >
          © 2026
        </div>
      </div>
    </AbsoluteFill>
  );
};
