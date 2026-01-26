/**
 * TARA Platform Scene - 3D brain visualization
 * Features: React Three Fiber brain, particle effects, glassmorphism cards
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { Brain2D } from '../components/Brain2D';
import { NeuralFlow } from '../components/NeuralFlow';
import { FloatingParticles } from '../components/Particles';
import { LettersPullUp, BlurInText } from '../components/TextAnimations';
import { colors } from '../data/oni-theme';

// Feature cards for TARA platform - professional icons for academic audience
const features = [
  {
    title: 'Brain Topology',
    description: 'Real-time 3D visualization of neural activity patterns',
    iconType: 'topology' as const,
    color: colors.biology.L11,
  },
  {
    title: 'Attack Simulator',
    description: 'Test defenses across all 14 layers',
    iconType: 'attack' as const,
    color: colors.security.danger,
  },
  {
    title: 'NSAM Monitor',
    description: 'Neural Signal Assurance flags anomalies',
    iconType: 'monitor' as const,
    color: colors.security.safe,
  },
];

// Professional abstract icons (SVG-based)
const FeatureIcon: React.FC<{ type: 'topology' | 'attack' | 'monitor'; color: string }> = ({ type, color }) => {
  if (type === 'topology') {
    return (
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
        <circle cx="12" cy="12" r="3" stroke={color} strokeWidth="1.5" />
        <circle cx="12" cy="4" r="2" fill={color} />
        <circle cx="20" cy="12" r="2" fill={color} />
        <circle cx="12" cy="20" r="2" fill={color} />
        <circle cx="4" cy="12" r="2" fill={color} />
        <line x1="12" y1="6" x2="12" y2="9" stroke={color} strokeWidth="1" />
        <line x1="18" y1="12" x2="15" y2="12" stroke={color} strokeWidth="1" />
        <line x1="12" y1="18" x2="12" y2="15" stroke={color} strokeWidth="1" />
        <line x1="6" y1="12" x2="9" y2="12" stroke={color} strokeWidth="1" />
      </svg>
    );
  }
  if (type === 'attack') {
    return (
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
        <path d="M12 2L15 8H21L16 12L18 20L12 16L6 20L8 12L3 8H9L12 2Z" stroke={color} strokeWidth="1.5" fill="none" />
        <circle cx="12" cy="11" r="2" fill={color} />
      </svg>
    );
  }
  return (
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
      <path d="M12 3L20 7V11C20 16 16 20 12 21C8 20 4 16 4 11V7L12 3Z" stroke={color} strokeWidth="1.5" fill="none" />
      <path d="M9 12L11 14L15 10" stroke={color} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
};

export const TARAScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Phase control
  const showBrain = frame > 80;
  const showFeatures = frame > 250;

  // Title animation
  const titleProgress = spring({
    frame,
    fps,
    config: { damping: 20, stiffness: 80 },
  });

  // Brain fade in
  const brainProgress = spring({
    frame: frame - 80,
    fps,
    config: { damping: 30, stiffness: 60 },
  });

  // Subtle glow pulse
  const glowPulse = interpolate(
    Math.sin(frame * 0.05),
    [-1, 1],
    [0.3, 0.6]
  );

  return (
    <AbsoluteFill
      style={{
        background: colors.gradients.innovation,
      }}
    >
      {/* Subtle particles */}
      <FloatingParticles
        count={50}
        color={colors.primary.accent}
        speed={0.15}
        minSize={1}
        maxSize={4}
      />

      {/* Content layout */}
      <div
        style={{
          display: 'flex',
          height: '100%',
          padding: 80,
          gap: 60,
        }}
      >
        {/* Left side - 3D Brain */}
        <div
          style={{
            flex: 1,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            opacity: Math.max(0, brainProgress),
            transform: `scale(${interpolate(
              Math.max(0, brainProgress),
              [0, 1],
              [0.9, 1]
            )})`,
          }}
        >
          {showBrain && (
            <div
              style={{
                filter: `drop-shadow(0 0 ${40 * glowPulse}px ${colors.primary.accent}44)`,
              }}
            >
              <Brain2D width={550} height={550} />
            </div>
          )}

          {/* Neural flow under brain */}
          <div style={{ marginTop: -40 }}>
            <NeuralFlow
              state={frame > 180 ? 'reactive' : 'resting'}
              width={350}
              height={45}
              intensity={0.5}
            />
          </div>
        </div>

        {/* Right side - Info */}
        <div
          style={{
            flex: 1,
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            gap: 40,
          }}
        >
          {/* TARA Title with letters pull-up */}
          <div
            style={{
              opacity: Math.max(0, titleProgress),
            }}
          >
            <LettersPullUp
              text="TARA"
              delay={0}
              fontSize={72}
              fontWeight={700}
              gradient={true}
            />

            <div style={{ marginTop: 12 }}>
              <BlurInText
                text="Telemetry Analysis & Response Automation"
                delay={20}
                fontSize={18}
                color={colors.text.muted}
                fontWeight={400}
              />
            </div>
          </div>

          {/* Feature cards with staggered animation */}
          {showFeatures && (
            <div
              style={{
                display: 'flex',
                flexDirection: 'column',
                gap: 16,
              }}
            >
              {features.map((feature, index) => {
                const cardProgress = spring({
                  frame: frame - 250 - index * 15,
                  fps,
                  config: { damping: 25, stiffness: 100 },
                });

                const cardX = interpolate(
                  Math.max(0, cardProgress),
                  [0, 1],
                  [80, 0]
                );

                return (
                  <div
                    key={feature.title}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: 20,
                      padding: 20,
                      background: `linear-gradient(135deg, rgba(255,255,255,0.04) 0%, rgba(255,255,255,0.01) 100%)`,
                      backdropFilter: 'blur(20px)',
                      borderRadius: 16,
                      border: `1px solid ${feature.color}22`,
                      opacity: Math.max(0, cardProgress),
                      transform: `translateX(${cardX}px)`,
                    }}
                  >
                    {/* Professional icon with subtle glow */}
                    <div
                      style={{
                        width: 52,
                        height: 52,
                        borderRadius: 14,
                        background: `${feature.color}15`,
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        boxShadow: `0 0 20px ${feature.color}33`,
                      }}
                    >
                      <FeatureIcon type={feature.iconType} color={feature.color} />
                    </div>

                    {/* Text */}
                    <div style={{ flex: 1 }}>
                      <div
                        style={{
                          fontSize: 18,
                          fontWeight: 600,
                          color: colors.text.primary,
                          marginBottom: 4,
                          letterSpacing: '-0.01em',
                        }}
                      >
                        {feature.title}
                      </div>
                      <div
                        style={{
                          fontSize: 14,
                          color: colors.text.muted,
                          lineHeight: 1.4,
                        }}
                      >
                        {feature.description}
                      </div>
                    </div>

                    {/* Status indicator */}
                    <div
                      style={{
                        width: 8,
                        height: 8,
                        borderRadius: '50%',
                        background: feature.color,
                        boxShadow: `0 0 10px ${feature.color}`,
                      }}
                    />
                  </div>
                );
              })}
            </div>
          )}

          {/* Open Source badge with smooth animation */}
          <div
            style={{
              opacity: interpolate(frame - 380, [0, 30], [0, 1], {
                extrapolateLeft: 'clamp',
                extrapolateRight: 'clamp',
              }),
              transform: `translateY(${interpolate(
                frame - 380,
                [0, 30],
                [20, 0],
                { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
              )}px)`,
            }}
          >
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 14,
                padding: '14px 20px',
                background: `${colors.security.safe}0a`,
                borderRadius: 12,
                border: `1px solid ${colors.security.safe}22`,
                width: 'fit-content',
              }}
            >
              <div
                style={{
                  width: 8,
                  height: 8,
                  borderRadius: '50%',
                  background: colors.security.safe,
                  boxShadow: `0 0 8px ${colors.security.safe}`,
                }}
              />
              <span
                style={{
                  color: colors.security.safe,
                  fontWeight: 600,
                  fontSize: 14,
                }}
              >
                100% Open Source
              </span>
              <span
                style={{
                  color: colors.text.muted,
                  fontSize: 14,
                }}
              >
                Apache 2.0
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Decorative corner elements */}
      <div
        style={{
          position: 'absolute',
          top: 40,
          right: 40,
          width: 60,
          height: 60,
          borderTop: `1px solid ${colors.primary.accent}33`,
          borderRight: `1px solid ${colors.primary.accent}33`,
          opacity: interpolate(frame, [0, 60], [0, 0.5], {
            extrapolateRight: 'clamp',
          }),
        }}
      />
    </AbsoluteFill>
  );
};
