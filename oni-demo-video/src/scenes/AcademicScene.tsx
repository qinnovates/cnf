import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, interpolate } from 'remotion';
import { TextReveal } from '../components/TextReveal';
import { colors, typography } from '../data/oni-theme';

// Academic citations and institutions
const citations = [
  {
    author: 'Kohno et al.',
    institution: 'University of Washington',
    paper: 'BCI Threat Modeling Framework',
    year: '2009',
  },
  {
    author: 'Martinovic et al.',
    institution: 'Columbia University',
    paper: 'Side-Channel BCI Attacks',
    year: '2012',
  },
  {
    author: 'Bonaci et al.',
    institution: 'Yale University',
    paper: 'App Stores for the Brain',
    year: '2015',
  },
  {
    author: 'Müller-Putz et al.',
    institution: 'Graz BCI Lab',
    paper: 'BCI Standardization Guidelines',
    year: '2021',
  },
];

export const AcademicScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <AbsoluteFill
      style={{
        background: colors.primary.dark,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 50,
      }}
    >
      {/* Title */}
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          gap: 16,
        }}
      >
        <TextReveal
          text="Built on Academic Foundation"
          fontSize={typography.fontSize.heading}
          delay={0}
        />
        <TextReveal
          text="Every claim is cited. Every formula is documented."
          fontSize={typography.fontSize.body}
          color={colors.text.secondary}
          delay={20}
        />
      </div>

      {/* Citation grid */}
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(2, 1fr)',
          gap: 30,
          maxWidth: 1200,
          marginTop: 30,
        }}
      >
        {citations.map((citation, index) => {
          const cardOpacity = spring({
            frame: frame - 60 - index * 20,
            fps,
            config: { damping: 100 },
          });

          const slideX = interpolate(
            spring({
              frame: frame - 60 - index * 20,
              fps,
              config: { damping: 20, stiffness: 100 },
            }),
            [0, 1],
            [index % 2 === 0 ? -50 : 50, 0]
          );

          return (
            <div
              key={citation.author}
              style={{
                padding: 28,
                backgroundColor: 'rgba(255, 255, 255, 0.03)',
                borderRadius: 16,
                border: `1px solid ${colors.primary.light}33`,
                opacity: Math.max(0, cardOpacity),
                transform: `translateX(${slideX}px)`,
              }}
            >
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'flex-start',
                  marginBottom: 12,
                }}
              >
                <div
                  style={{
                    fontSize: typography.fontSize.body,
                    color: colors.primary.accent,
                    fontWeight: 600,
                  }}
                >
                  {citation.author}
                </div>
                <div
                  style={{
                    fontSize: typography.fontSize.small,
                    color: colors.text.muted,
                    fontFamily: typography.fontFamily.mono,
                  }}
                >
                  {citation.year}
                </div>
              </div>

              <div
                style={{
                  fontSize: typography.fontSize.small,
                  color: colors.text.secondary,
                  marginBottom: 8,
                }}
              >
                {citation.institution}
              </div>

              <div
                style={{
                  fontSize: typography.fontSize.small,
                  color: colors.text.muted,
                  fontStyle: 'italic',
                }}
              >
                "{citation.paper}"
              </div>
            </div>
          );
        })}
      </div>

      {/* Research logos/badges */}
      <div
        style={{
          display: 'flex',
          gap: 60,
          marginTop: 40,
          opacity: spring({ frame: frame - 200, fps, config: { damping: 100 } }),
        }}
      >
        {['Peer Reviewed', 'IEEE Cited', 'Open Research'].map((badge, index) => (
          <div
            key={badge}
            style={{
              padding: '12px 24px',
              backgroundColor: 'rgba(255, 255, 255, 0.05)',
              borderRadius: 8,
              fontSize: typography.fontSize.small,
              color: colors.text.secondary,
              fontWeight: 500,
              opacity: spring({
                frame: frame - 200 - index * 10,
                fps,
                config: { damping: 100 },
              }),
            }}
          >
            ✓ {badge}
          </div>
        ))}
      </div>
    </AbsoluteFill>
  );
};
