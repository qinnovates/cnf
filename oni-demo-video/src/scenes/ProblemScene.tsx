/**
 * Problem Scene - Sets up the challenge BCIs face
 * Features: Staggered reveals, clean typography, smooth transitions
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { FloatingParticles } from '../components/Particles';
import { WordsStaggerFade, LettersPullUp, GlowingText, BlurInText } from '../components/TextAnimations';
import { colors, typography } from '../data/oni-theme';

const problemStatements = [
  { text: 'BCIs exist today', delay: 0 },
  { text: 'But there are no security standards', delay: 45 },
  { text: 'No common language', delay: 90 },
  { text: 'No shared framework', delay: 135 },
];

export const ProblemScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Phase transitions
  const showUntilNow = frame > 400;
  const showIntro = frame > 520;

  // Background pulse intensity
  const pulseIntensity = interpolate(
    Math.sin(frame * 0.03),
    [-1, 1],
    [0.02, 0.06]
  );

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at center, ${colors.primary.main}${Math.round(pulseIntensity * 255).toString(16).padStart(2, '0')} 0%, ${colors.primary.dark} 70%)`,
      }}
    >
      {/* Subtle particles */}
      <FloatingParticles
        count={30}
        color={colors.security.danger}
        speed={0.15}
        minSize={1}
        maxSize={3}
      />

      {/* Problem statements */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          gap: 50,
          alignItems: 'flex-start',
          justifyContent: 'center',
          height: '100%',
          paddingLeft: 200,
          opacity: showUntilNow
            ? interpolate(frame - 400, [0, 30], [1, 0.15], {
                extrapolateRight: 'clamp',
              })
            : 1,
          transform: showUntilNow
            ? `scale(${interpolate(frame - 400, [0, 30], [1, 0.9], {
                extrapolateRight: 'clamp',
              })})`
            : 'scale(1)',
        }}
      >
        {problemStatements.map((statement, index) => {
          const entryProgress = spring({
            frame: frame - statement.delay,
            fps,
            config: { damping: 25, stiffness: 80 },
          });

          const showX = frame > statement.delay + 40;

          const xProgress = spring({
            frame: frame - statement.delay - 40,
            fps,
            config: { damping: 15, stiffness: 200 },
          });

          return (
            <div
              key={index}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 30,
                opacity: Math.max(0, entryProgress),
                transform: `translateX(${interpolate(
                  Math.max(0, entryProgress),
                  [0, 1],
                  [50, 0]
                )}px)`,
              }}
            >
              {/* X mark with animation */}
              <div
                style={{
                  width: 44,
                  height: 44,
                  borderRadius: '50%',
                  backgroundColor: showX
                    ? `${colors.security.danger}22`
                    : 'transparent',
                  border: `2px solid ${showX ? colors.security.danger : colors.text.muted}55`,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  transform: `scale(${showX ? Math.max(0, xProgress) : 0.8})`,
                  boxShadow: showX
                    ? `0 0 20px ${colors.security.danger}33`
                    : 'none',
                }}
              >
                {showX && (
                  <span
                    style={{
                      color: colors.security.danger,
                      fontSize: 22,
                      fontWeight: 600,
                      opacity: Math.max(0, xProgress),
                    }}
                  >
                    ✕
                  </span>
                )}
              </div>

              {/* Statement text */}
              <div
                style={{
                  fontSize: 42,
                  fontWeight: 500,
                  color: colors.text.primary,
                  letterSpacing: '-0.01em',
                }}
              >
                {statement.text}
              </div>
            </div>
          );
        })}
      </div>

      {/* "Until now" reveal */}
      {showUntilNow && !showIntro && (
        <div
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
          }}
        >
          <LettersPullUp
            text="Until now."
            delay={0}
            fontSize={88}
            fontWeight={700}
            gradient={false}
          />
        </div>
      )}

      {/* ONI Introduction */}
      {showIntro && (
        <div
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            gap: 30,
          }}
        >
          {/* Introducing label */}
          <div
            style={{
              overflow: 'hidden',
            }}
          >
            <BlurInText
              text="INTRODUCING"
              delay={0}
              fontSize={18}
              color={colors.text.muted}
              fontWeight={500}
            />
          </div>

          {/* ONI Framework title */}
          <LettersPullUp
            text="Open Neural Interface"
            delay={15}
            fontSize={72}
            fontWeight={700}
            gradient={true}
          />

          {/* Framework subtitle */}
          <BlurInText
            text="Framework"
            delay={40}
            fontSize={56}
            fontWeight={300}
            gradient={true}
          />
        </div>
      )}

      {/* Side accent line */}
      <div
        style={{
          position: 'absolute',
          left: 100,
          top: '20%',
          bottom: '20%',
          width: 2,
          background: `linear-gradient(transparent, ${colors.security.danger}44, transparent)`,
          opacity: showUntilNow ? 0 : 1,
        }}
      />

      {/* Bottom gradient */}
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: 200,
          background: `linear-gradient(transparent, ${colors.primary.dark}cc)`,
          pointerEvents: 'none',
        }}
      />
    </AbsoluteFill>
  );
};
