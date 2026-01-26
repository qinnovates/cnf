/**
 * Title Scene with Threads - Brain Wave Animation
 * Abstract vector-like waves resembling neural activity
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { Threads, SplitText, GradientText, BlurText } from '../components/reactbits';
import { colors } from '../data/oni-theme';

export const TitleThreadsScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Animation phases
  const showONI = frame >= 45;
  const showTagline = frame >= 100;
  const showSubtitle = frame >= 140;

  // ONI scale with spring
  const oniScale = spring({
    frame: frame - 45,
    fps,
    config: { damping: 12, stiffness: 50, mass: 1.2 },
  });

  // Glow pulse
  const glowPulse = interpolate(
    Math.sin(frame * 0.05),
    [-1, 1],
    [0.4, 1]
  );

  // Thread animation speeds up slightly over time
  const threadSpeed = interpolate(frame, [0, 180], [0.5, 1.2], {
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{ background: colors.primary.dark }}>
      {/* Primary Threads layer - Blue brain waves */}
      <Threads
        color="#0088cc"
        secondaryColor="#00e5ff"
        lineCount={18}
        amplitude={100}
        speed={threadSpeed}
        frequency={0.8}
        blur={4}
        opacity={0.5}
      />

      {/* Secondary Threads layer - Purple accent waves */}
      <div style={{ opacity: 0.4 }}>
        <Threads
          color="#7c3aed"
          secondaryColor="#a855f7"
          lineCount={12}
          amplitude={60}
          speed={threadSpeed * 0.7}
          frequency={1.2}
          blur={6}
          opacity={0.4}
        />
      </div>

      {/* Subtle top layer - White highlights */}
      <div style={{ opacity: 0.15 }}>
        <Threads
          color="#ffffff"
          secondaryColor="#00e5ff"
          lineCount={8}
          amplitude={40}
          speed={threadSpeed * 1.3}
          frequency={1.5}
          blur={2}
          opacity={0.3}
        />
      </div>

      {/* Central gradient overlay for depth */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: `radial-gradient(ellipse at center, transparent 0%, ${colors.primary.dark}90 70%, ${colors.primary.dark} 100%)`,
          pointerEvents: 'none',
        }}
      />

      {/* Content container */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          gap: 24,
        }}
      >
        {/* ONI Logo */}
        {showONI && (
          <div
            style={{
              transform: `scale(${Math.max(0, oniScale)})`,
              filter: `drop-shadow(0 0 ${80 * glowPulse}px ${colors.primary.accent}55)`,
            }}
          >
            <SplitText
              text="ONI"
              delay={45}
              direction="up"
              staggerDelay={10}
              style={{
                fontSize: 220,
                fontWeight: 800,
                fontFamily: "'Inter', 'Helvetica Neue', sans-serif",
                letterSpacing: '-0.03em',
                background: `linear-gradient(180deg,
                  #ffffff 0%,
                  #ffffff 20%,
                  ${colors.primary.accent} 60%,
                  ${colors.primary.accentPurple} 100%
                )`,
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
              }}
            />
          </div>
        )}

        {/* Tagline */}
        {showTagline && (
          <GradientText
            text="Open Neurocomputing Interface"
            delay={100}
            colors={['#00e5ff', '#a855f7', '#00e5ff']}
            speed={0.4}
            style={{
              fontSize: 26,
              fontWeight: 300,
              letterSpacing: '0.35em',
              textTransform: 'uppercase',
            }}
          />
        )}

        {/* Subtitle */}
        {showSubtitle && (
          <BlurText
            text="The OSI of Mind"
            delay={140}
            animateBy="word"
            staggerDelay={12}
            style={{
              fontSize: 18,
              fontWeight: 400,
              letterSpacing: '0.2em',
              color: colors.text.muted,
              marginTop: 8,
            }}
          />
        )}
      </div>

      {/* Bottom fade for text readability */}
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: 200,
          background: `linear-gradient(transparent, ${colors.primary.dark})`,
          pointerEvents: 'none',
        }}
      />

      {/* Top fade */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          height: 150,
          background: `linear-gradient(${colors.primary.dark}, transparent)`,
          pointerEvents: 'none',
        }}
      />
    </AbsoluteFill>
  );
};

export default TitleThreadsScene;
