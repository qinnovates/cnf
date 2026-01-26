import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { TextReveal } from '../components/TextReveal';
import { colors, typography } from '../data/oni-theme';

export const CTAScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Terminal typing animation for pip command
  const pipCommand = "pip install oni-framework";
  const typedLength = Math.min(
    pipCommand.length,
    Math.floor(interpolate(frame, [150, 300], [0, pipCommand.length], { extrapolateRight: 'clamp' }))
  );

  // Cursor blink
  const cursorVisible = Math.floor(frame / 15) % 2 === 0;

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at center, ${colors.primary.main}33 0%, ${colors.primary.dark} 70%)`,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 50,
      }}
    >
      {/* Main CTA */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: 24,
        }}
      >
        <TextReveal
          text="Ready to secure the neural frontier?"
          fontSize={typography.fontSize.heading}
          delay={0}
        />
      </div>

      {/* Terminal window */}
      <div
        style={{
          marginTop: 30,
          opacity: spring({ frame: frame - 100, fps, config: { damping: 100 } }),
          transform: `scale(${interpolate(
            spring({ frame: frame - 100, fps, config: { damping: 20 } }),
            [0, 1],
            [0.9, 1]
          )})`,
        }}
      >
        {/* Terminal header */}
        <div
          style={{
            backgroundColor: '#2d2d2d',
            padding: '12px 20px',
            borderTopLeftRadius: 12,
            borderTopRightRadius: 12,
            display: 'flex',
            gap: 8,
          }}
        >
          <div style={{ width: 12, height: 12, borderRadius: '50%', backgroundColor: '#ff5f56' }} />
          <div style={{ width: 12, height: 12, borderRadius: '50%', backgroundColor: '#ffbd2e' }} />
          <div style={{ width: 12, height: 12, borderRadius: '50%', backgroundColor: '#27c93f' }} />
        </div>

        {/* Terminal body */}
        <div
          style={{
            backgroundColor: '#1a1a1a',
            padding: '30px 40px',
            borderBottomLeftRadius: 12,
            borderBottomRightRadius: 12,
            fontFamily: typography.fontFamily.mono,
            fontSize: typography.fontSize.subheading,
            minWidth: 600,
          }}
        >
          <span style={{ color: colors.security.safe }}>$ </span>
          <span style={{ color: colors.text.primary }}>
            {pipCommand.slice(0, typedLength)}
          </span>
          {cursorVisible && typedLength < pipCommand.length && (
            <span
              style={{
                backgroundColor: colors.text.primary,
                width: 12,
                height: 28,
                display: 'inline-block',
                marginLeft: 2,
              }}
            />
          )}
        </div>
      </div>

      {/* Action buttons */}
      <div
        style={{
          display: 'flex',
          gap: 30,
          marginTop: 40,
        }}
      >
        {[
          { label: 'View on GitHub', icon: '📦', primary: true },
          { label: 'Read the Docs', icon: '📚', primary: false },
          { label: 'Join Community', icon: '🤝', primary: false },
        ].map((button, index) => {
          const buttonOpacity = spring({
            frame: frame - 300 - index * 15,
            fps,
            config: { damping: 100 },
          });

          return (
            <div
              key={button.label}
              style={{
                padding: '20px 40px',
                backgroundColor: button.primary ? colors.primary.accent : 'transparent',
                border: `2px solid ${button.primary ? colors.primary.accent : colors.text.muted}`,
                borderRadius: 12,
                display: 'flex',
                alignItems: 'center',
                gap: 12,
                opacity: Math.max(0, buttonOpacity),
                cursor: 'pointer',
              }}
            >
              <span style={{ fontSize: 24 }}>{button.icon}</span>
              <span
                style={{
                  fontSize: typography.fontSize.body,
                  color: button.primary ? colors.primary.dark : colors.text.primary,
                  fontWeight: 600,
                }}
              >
                {button.label}
              </span>
            </div>
          );
        })}
      </div>

      {/* GitHub URL */}
      <div
        style={{
          marginTop: 30,
          fontSize: typography.fontSize.body,
          color: colors.text.muted,
          fontFamily: typography.fontFamily.mono,
          opacity: spring({ frame: frame - 400, fps, config: { damping: 100 } }),
        }}
      >
        github.com/qikevinl/oni
      </div>
    </AbsoluteFill>
  );
};
