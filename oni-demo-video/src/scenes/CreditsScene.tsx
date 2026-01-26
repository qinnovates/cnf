import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, Img, staticFile } from 'remotion';
import { colors, typography } from '../data/oni-theme';

export const CreditsScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Fade in
  const fadeIn = spring({
    frame,
    fps,
    config: { damping: 100 },
  });

  // Logo pulse
  const logoScale = 1 + Math.sin(frame * 0.1) * 0.02;

  return (
    <AbsoluteFill
      style={{
        background: colors.primary.dark,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 40,
        opacity: Math.max(0, fadeIn),
      }}
    >
      {/* ONI Logo */}
      <div
        style={{
          transform: `scale(${logoScale})`,
        }}
      >
        <Img
          src={staticFile("assets/ONI_Logo.png")}
          style={{
            width: 200,
            objectFit: 'contain',
          }}
        />
      </div>

      {/* Title */}
      <div
        style={{
          fontSize: typography.fontSize.heading,
          fontWeight: 700,
          color: colors.text.primary,
          textAlign: 'center',
        }}
      >
        Open Neural Interface Framework
      </div>

      {/* Tagline */}
      <div
        style={{
          fontSize: typography.fontSize.subtitle,
          color: colors.primary.accent,
          letterSpacing: '0.15em',
        }}
      >
        The OSI of Mind
      </div>

      {/* Divider */}
      <div
        style={{
          width: 200,
          height: 2,
          backgroundColor: colors.primary.accent,
          opacity: 0.3,
          margin: '20px 0',
        }}
      />

      {/* Credits info */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: 16,
        }}
      >
        <div
          style={{
            fontSize: typography.fontSize.body,
            color: colors.text.secondary,
          }}
        >
          Created by <span style={{ color: colors.text.primary, fontWeight: 600 }}>Kevin Qi</span>
        </div>

        <div
          style={{
            fontSize: typography.fontSize.small,
            color: colors.text.muted,
          }}
        >
          Apache 2.0 License
        </div>
      </div>

      {/* Built with Claude badge */}
      <div
        style={{
          marginTop: 40,
          padding: '12px 24px',
          backgroundColor: 'rgba(255, 255, 255, 0.05)',
          borderRadius: 8,
          display: 'flex',
          alignItems: 'center',
          gap: 12,
          opacity: spring({ frame: frame - 30, fps, config: { damping: 100 } }),
        }}
      >
        <span
          style={{
            fontSize: typography.fontSize.small,
            color: colors.text.muted,
          }}
        >
          Built with
        </span>
        <span
          style={{
            fontSize: typography.fontSize.small,
            color: colors.primary.accent,
            fontWeight: 600,
          }}
        >
          Claude Code
        </span>
      </div>

      {/* Year */}
      <div
        style={{
          position: 'absolute',
          bottom: 40,
          fontSize: typography.fontSize.small,
          color: colors.text.muted,
        }}
      >
        © 2026
      </div>
    </AbsoluteFill>
  );
};
