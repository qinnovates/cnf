/**
 * Title Scene - Apple-quality logo reveal with animated ONI branding
 * Features: Custom animated logo, circular waves, spring physics
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { AnimatedONILogo, CircularWaves } from '../components/AnimatedONILogo';
import { NeuralFlow } from '../components/NeuralFlow';
import { FloatingParticles } from '../components/Particles';
import { colors } from '../data/oni-theme';

export const TitleScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Scene fade in
  const sceneOpacity = spring({
    frame,
    fps,
    config: { damping: 50, stiffness: 100 },
  });

  // Neural flow activation timing
  const flowState = frame > 60 ? 'reactive' : 'resting';

  // Subtle ambient movement
  const ambientShift = Math.sin(frame * 0.02) * 5;

  return (
    <AbsoluteFill
      style={{
        background: colors.gradients.background,
        opacity: Math.max(0, sceneOpacity),
      }}
    >
      {/* Circular wave background */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          opacity: 0.4,
        }}
      >
        <CircularWaves
          numWaves={6}
          baseRadius={150}
          color={colors.primary.accent}
        />
      </div>

      {/* Secondary wave layer with different color */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          opacity: 0.2,
        }}
      >
        <CircularWaves
          numWaves={4}
          baseRadius={200}
          color={colors.gateway.L8}
        />
      </div>

      {/* Floating particles */}
      <FloatingParticles
        count={60}
        color={colors.primary.accent}
        speed={0.15}
        minSize={1}
        maxSize={4}
      />

      {/* Main content */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          height: '100%',
          transform: `translateY(${ambientShift}px)`,
        }}
      >
        {/* Animated ONI Logo */}
        <div style={{ marginTop: -80 }}>
          <AnimatedONILogo
            width={700}
            height={500}
            showText={true}
          />
        </div>

        {/* Neural Flow under logo */}
        <div
          style={{
            marginTop: 40,
            opacity: interpolate(frame, [50, 70], [0, 1], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
          }}
        >
          <NeuralFlow
            state={flowState}
            width={500}
            height={50}
            intensity={0.7}
          />
        </div>
      </div>

      {/* Decorative corner brackets */}
      {[
        { top: 60, left: 60, rotate: 0 },
        { top: 60, right: 60, rotate: 90 },
        { bottom: 60, right: 60, rotate: 180 },
        { bottom: 60, left: 60, rotate: 270 },
      ].map((pos, i) => {
        const bracketProgress = spring({
          frame: frame - 80 - i * 8,
          fps,
          config: { damping: 25, stiffness: 80 },
        });

        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              top: pos.top,
              left: pos.left,
              right: pos.right,
              bottom: pos.bottom,
              width: 40,
              height: 40,
              opacity: Math.max(0, bracketProgress) * 0.4,
              transform: `rotate(${pos.rotate}deg) scale(${interpolate(
                Math.max(0, bracketProgress),
                [0, 1],
                [0.5, 1]
              )})`,
            }}
          >
            <svg width="40" height="40" viewBox="0 0 40 40">
              <path
                d="M 0 20 L 0 0 L 20 0"
                stroke={colors.primary.accent}
                strokeWidth="1"
                fill="none"
                opacity="0.6"
              />
            </svg>
          </div>
        );
      })}

      {/* Gradient overlays for depth */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          height: 200,
          background: `linear-gradient(${colors.primary.dark}88, transparent)`,
          pointerEvents: 'none',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: 200,
          background: `linear-gradient(transparent, ${colors.primary.dark}88)`,
          pointerEvents: 'none',
        }}
      />
    </AbsoluteFill>
  );
};
