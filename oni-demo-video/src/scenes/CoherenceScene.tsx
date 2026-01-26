import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { CoherenceGauge } from '../components/CoherenceGauge';
import { TextReveal } from '../components/TextReveal';
import { colors, typography } from '../data/oni-theme';

export const CoherenceScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Animate coherence value over time
  const coherenceValue = interpolate(
    frame,
    [0, 300, 600, 900],
    [0.45, 0.85, 0.92, 0.85],
    { extrapolateRight: 'clamp' }
  );

  // Show interactive demo hint after main animation
  const showDemo = frame > 600;
  const demoOpacity = spring({
    frame: frame - 600,
    fps,
    config: { damping: 100 },
  });

  return (
    <AbsoluteFill
      style={{
        background: colors.primary.dark,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 60,
      }}
    >
      {/* Title */}
      <TextReveal
        text="The Coherence Score"
        fontSize={typography.fontSize.heading}
        delay={0}
      />

      {/* Subtitle */}
      <TextReveal
        text="A unified metric for neural security"
        fontSize={typography.fontSize.body}
        color={colors.text.secondary}
        delay={15}
      />

      {/* Coherence gauge */}
      <CoherenceGauge value={coherenceValue} showFormula={true} animated={true} />

      {/* Interactive demo callout */}
      {showDemo && (
        <div
          style={{
            marginTop: 40,
            padding: '20px 40px',
            backgroundColor: `${colors.primary.accent}11`,
            borderRadius: 12,
            border: `1px solid ${colors.primary.accent}44`,
            display: 'flex',
            alignItems: 'center',
            gap: 16,
            opacity: Math.max(0, demoOpacity),
          }}
        >
          <div
            style={{
              width: 12,
              height: 12,
              borderRadius: '50%',
              backgroundColor: colors.security.safe,
              boxShadow: `0 0 10px ${colors.security.safe}`,
              animation: 'pulse 2s infinite',
            }}
          />
          <span
            style={{
              fontSize: typography.fontSize.body,
              color: colors.text.secondary,
            }}
          >
            Try it yourself in the
          </span>
          <span
            style={{
              fontSize: typography.fontSize.body,
              color: colors.primary.accent,
              fontWeight: 600,
            }}
          >
            Interactive Playground →
          </span>
        </div>
      )}

      {/* Component explanation cards */}
      <div
        style={{
          display: 'flex',
          gap: 30,
          marginTop: 20,
          opacity: spring({ frame: frame - 200, fps, config: { damping: 100 } }),
        }}
      >
        {[
          { label: 'Φ Phase Sync', desc: 'Neural oscillation alignment' },
          { label: 'Δt Timing', desc: 'Temporal precision' },
          { label: 'Θ Frequency', desc: 'Band-specific response' },
        ].map((item, index) => (
          <div
            key={item.label}
            style={{
              padding: 20,
              backgroundColor: 'rgba(255, 255, 255, 0.05)',
              borderRadius: 12,
              textAlign: 'center',
              width: 200,
              opacity: spring({
                frame: frame - 200 - index * 10,
                fps,
                config: { damping: 100 },
              }),
            }}
          >
            <div
              style={{
                fontSize: typography.fontSize.body,
                color: colors.primary.accent,
                fontFamily: typography.fontFamily.mono,
                marginBottom: 8,
              }}
            >
              {item.label}
            </div>
            <div
              style={{
                fontSize: typography.fontSize.small,
                color: colors.text.muted,
              }}
            >
              {item.desc}
            </div>
          </div>
        ))}
      </div>
    </AbsoluteFill>
  );
};
