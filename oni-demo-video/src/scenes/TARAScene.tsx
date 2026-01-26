/**
 * TARA Platform Scene - 3D brain visualization
 * Features: React Three Fiber brain, particle effects, glassmorphism cards
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { Brain3D } from '../components/Brain3D';
import { NeuralFlow } from '../components/NeuralFlow';
import { FloatingParticles } from '../components/Particles';
import { SlideIn } from '../components/Transitions';
import { colors, typography } from '../data/oni-theme';

// Feature cards for TARA platform
const features = [
  {
    title: 'Brain Topology',
    description: 'Real-time 3D visualization of neural activity patterns',
    icon: '🧠',
    color: colors.biology.L11,
  },
  {
    title: 'Attack Simulator',
    description: 'Test defenses across all 14 layers',
    icon: '⚔️',
    color: colors.security.danger,
  },
  {
    title: 'NSAM Monitor',
    description: 'Neural Signal Assurance flags anomalies',
    icon: '🛡️',
    color: colors.security.safe,
  },
];

export const TARAScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Phase control
  const showBrain = frame > 100;
  const showFeatures = frame > 300;

  // Title animation
  const titleScale = spring({
    frame,
    fps,
    config: { damping: 15, stiffness: 100 },
  });

  // Brain fade in
  const brainOpacity = spring({
    frame: frame - 100,
    fps,
    config: { damping: 100 },
  });

  return (
    <AbsoluteFill
      style={{
        background: `linear-gradient(135deg, ${colors.primary.dark} 0%, ${colors.primary.main}33 100%)`,
      }}
    >
      {/* Subtle particles */}
      <FloatingParticles count={40} color={colors.primary.accent} speed={0.2} />

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
            opacity: Math.max(0, brainOpacity),
          }}
        >
          {showBrain && <Brain3D width={700} height={700} />}

          {/* Neural flow under brain */}
          <div style={{ marginTop: -60 }}>
            <NeuralFlow
              state={frame > 200 ? 'reactive' : 'resting'}
              width={400}
              height={50}
              intensity={0.6}
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
          {/* TARA Title */}
          <div
            style={{
              transform: `scale(${Math.max(0, titleScale)})`,
            }}
          >
            <div
              style={{
                fontSize: 80,
                fontWeight: 700,
                background: `linear-gradient(135deg, ${colors.text.primary} 0%, ${colors.primary.accent} 100%)`,
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
                marginBottom: 8,
              }}
            >
              TARA
            </div>
            <div
              style={{
                fontSize: typography.fontSize.body,
                color: colors.text.secondary,
                letterSpacing: '0.05em',
              }}
            >
              Threat Assessment & Risk Analysis Platform
            </div>
          </div>

          {/* Feature cards */}
          {showFeatures && (
            <div
              style={{
                display: 'flex',
                flexDirection: 'column',
                gap: 20,
              }}
            >
              {features.map((feature, index) => {
                const cardProgress = spring({
                  frame: frame - 300 - index * 20,
                  fps,
                  config: { damping: 20, stiffness: 100 },
                });

                const cardX = interpolate(
                  Math.max(0, cardProgress),
                  [0, 1],
                  [100, 0]
                );

                return (
                  <div
                    key={feature.title}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: 20,
                      padding: 24,
                      background: 'rgba(255, 255, 255, 0.03)',
                      backdropFilter: 'blur(20px)',
                      borderRadius: 16,
                      border: `1px solid ${feature.color}33`,
                      opacity: Math.max(0, cardProgress),
                      transform: `translateX(${cardX}px)`,
                    }}
                  >
                    {/* Icon with glow */}
                    <div
                      style={{
                        width: 56,
                        height: 56,
                        borderRadius: 12,
                        background: `${feature.color}22`,
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: 28,
                        boxShadow: `0 0 20px ${feature.color}44`,
                      }}
                    >
                      {feature.icon}
                    </div>

                    {/* Text */}
                    <div>
                      <div
                        style={{
                          fontSize: typography.fontSize.body,
                          fontWeight: 600,
                          color: colors.text.primary,
                          marginBottom: 4,
                        }}
                      >
                        {feature.title}
                      </div>
                      <div
                        style={{
                          fontSize: typography.fontSize.small,
                          color: colors.text.muted,
                        }}
                      >
                        {feature.description}
                      </div>
                    </div>

                    {/* Status indicator */}
                    <div
                      style={{
                        marginLeft: 'auto',
                        width: 10,
                        height: 10,
                        borderRadius: '50%',
                        background: feature.color,
                        boxShadow: `0 0 10px ${feature.color}`,
                        animation: 'pulse 2s infinite',
                      }}
                    />
                  </div>
                );
              })}
            </div>
          )}

          {/* Open Source badge */}
          <SlideIn direction="up" delay={400}>
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 16,
                padding: '16px 24px',
                background: `${colors.security.safe}11`,
                borderRadius: 12,
                border: `1px solid ${colors.security.safe}33`,
                width: 'fit-content',
              }}
            >
              <div
                style={{
                  width: 8,
                  height: 8,
                  borderRadius: '50%',
                  background: colors.security.safe,
                  boxShadow: `0 0 10px ${colors.security.safe}`,
                }}
              />
              <span style={{ color: colors.security.safe, fontWeight: 600 }}>
                100% Open Source
              </span>
              <span style={{ color: colors.text.muted }}>
                Apache 2.0
              </span>
            </div>
          </SlideIn>
        </div>
      </div>
    </AbsoluteFill>
  );
};
