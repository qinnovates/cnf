/**
 * Problem Scene - Sets up the challenge BCIs face
 * Features: Fact vs Problem distinction, clean design, smooth transitions
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { FloatingParticles } from '../components/Particles';
import { LettersPullUp, BlurInText } from '../components/TextAnimations';
import { colors } from '../data/oni-theme';

// Statements with type distinction
const statements = [
  {
    text: 'Brain-computer interfaces are here',
    type: 'fact' as const,
    delay: 0,
    subtext: 'FDA approved, in clinical trials'
  },
  {
    text: 'No standardized security framework',
    type: 'problem' as const,
    delay: 60,
    subtext: null
  },
  {
    text: 'No common language across disciplines',
    type: 'problem' as const,
    delay: 120,
    subtext: null
  },
  {
    text: 'No shared threat model',
    type: 'problem' as const,
    delay: 180,
    subtext: null
  },
];

export const ProblemScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Phase transitions
  const showUntilNow = frame > 450;
  const showIntro = frame > 570;

  // Background pulse
  const pulseIntensity = interpolate(
    Math.sin(frame * 0.03),
    [-1, 1],
    [0.15, 0.25]
  );

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at center, ${colors.primary.main}${Math.round(pulseIntensity * 255).toString(16).padStart(2, '0')} 0%, ${colors.primary.darkPurple} 50%, ${colors.primary.dark} 100%)`,
      }}
    >
      {/* Subtle particles */}
      <FloatingParticles
        count={25}
        color={colors.primary.accent}
        speed={0.12}
        minSize={1}
        maxSize={2}
      />

      {/* Problem statements */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          gap: 36,
          alignItems: 'flex-start',
          justifyContent: 'center',
          height: '100%',
          paddingLeft: 180,
          opacity: showUntilNow
            ? interpolate(frame - 450, [0, 30], [1, 0], {
                extrapolateRight: 'clamp',
              })
            : 1,
          transform: showUntilNow
            ? `scale(${interpolate(frame - 450, [0, 30], [1, 0.95], {
                extrapolateRight: 'clamp',
              })})`
            : 'scale(1)',
        }}
      >
        {statements.map((statement, index) => {
          const entryProgress = spring({
            frame: frame - statement.delay,
            fps,
            config: { damping: 25, stiffness: 80 },
          });

          const iconDelay = statement.delay + 30;
          const iconProgress = spring({
            frame: frame - iconDelay,
            fps,
            config: { damping: 15, stiffness: 150 },
          });

          const isFact = statement.type === 'fact';
          const iconColor = isFact ? colors.security.safe : colors.security.warning;
          const showIcon = frame > iconDelay;

          return (
            <div
              key={index}
              style={{
                opacity: Math.max(0, entryProgress),
                transform: `translateX(${interpolate(
                  Math.max(0, entryProgress),
                  [0, 1],
                  [40, 0]
                )}px)`,
              }}
            >
              <div
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 24,
                }}
              >
                {/* Icon - checkmark for fact, warning for problem */}
                <div
                  style={{
                    width: 40,
                    height: 40,
                    borderRadius: isFact ? '50%' : 8,
                    backgroundColor: showIcon ? `${iconColor}15` : 'transparent',
                    border: `2px solid ${showIcon ? iconColor : colors.text.muted}44`,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    transform: `scale(${showIcon ? Math.max(0, iconProgress) : 0.8})`,
                    boxShadow: showIcon ? `0 0 20px ${iconColor}22` : 'none',
                  }}
                >
                  {showIcon && (
                    <span
                      style={{
                        color: iconColor,
                        fontSize: isFact ? 20 : 18,
                        fontWeight: 600,
                        opacity: Math.max(0, iconProgress),
                      }}
                    >
                      {isFact ? '✓' : '!'}
                    </span>
                  )}
                </div>

                {/* Statement text */}
                <div
                  style={{
                    fontSize: 38,
                    fontWeight: isFact ? 600 : 500,
                    color: isFact ? colors.text.primary : colors.text.secondary,
                    letterSpacing: '-0.01em',
                  }}
                >
                  {statement.text}
                </div>
              </div>

              {/* Subtext for fact */}
              {statement.subtext && (
                <div
                  style={{
                    marginLeft: 64,
                    marginTop: 8,
                    fontSize: 16,
                    color: colors.text.muted,
                    fontWeight: 400,
                    opacity: interpolate(
                      frame - statement.delay - 20,
                      [0, 20],
                      [0, 0.8],
                      { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
                    ),
                  }}
                >
                  {statement.subtext}
                </div>
              )}
            </div>
          );
        })}

        {/* Divider line after fact, before problems */}
        <div
          style={{
            width: interpolate(frame - 50, [0, 40], [0, 500], {
              extrapolateLeft: 'clamp',
              extrapolateRight: 'clamp',
            }),
            height: 1,
            background: `linear-gradient(90deg, ${colors.text.muted}33, transparent)`,
            marginLeft: 64,
            marginTop: -12,
            marginBottom: -12,
            opacity: showUntilNow ? 0 : 1,
          }}
        />
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
          <div style={{ overflow: 'hidden' }}>
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

      {/* Decorative side element */}
      <div
        style={{
          position: 'absolute',
          left: 80,
          top: '25%',
          bottom: '25%',
          width: 3,
          borderRadius: 2,
          background: `linear-gradient(transparent, ${colors.primary.accent}44, ${colors.security.warning}44, transparent)`,
          opacity: showUntilNow ? 0 : 0.6,
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
