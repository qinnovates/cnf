import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, Img, staticFile, interpolate } from 'remotion';
import { LayerStack } from '../components/LayerStack';
import { TextReveal } from '../components/TextReveal';
import { colors, typography } from '../data/oni-theme';

export const LayersScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Phases of the scene
  const showHourglass = frame < 300;
  const showStack = frame >= 300;
  const highlightGateway = frame >= 600 && frame < 900;

  // Highlight which layer based on frame
  const getHighlightLayer = () => {
    if (frame >= 600 && frame < 750) return 8; // Gateway
    if (frame >= 900 && frame < 1000) return 14; // Identity
    if (frame >= 1000 && frame < 1100) return 1; // Physical
    return undefined;
  };

  // Hourglass opacity
  const hourglassOpacity = interpolate(
    frame,
    [0, 30, 270, 300],
    [0, 1, 1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  // Stack fade in
  const stackOpacity = spring({
    frame: frame - 300,
    fps,
    config: { damping: 100 },
  });

  return (
    <AbsoluteFill
      style={{
        background: colors.primary.dark,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      {/* Hourglass diagram from assets */}
      {showHourglass && (
        <div
          style={{
            opacity: hourglassOpacity,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: 40,
          }}
        >
          <TextReveal
            text="14 Layers: Silicon to Synapse"
            fontSize={typography.fontSize.heading}
            delay={0}
          />
          <Img
            src={staticFile("assets/ONI_Layers_Diagram-HOURGLASS.png")}
            style={{
              maxWidth: 900,
              maxHeight: 700,
              objectFit: 'contain',
            }}
          />
        </div>
      )}

      {/* Interactive layer stack */}
      {showStack && (
        <div
          style={{
            display: 'flex',
            gap: 100,
            alignItems: 'center',
            opacity: Math.max(0, stackOpacity),
          }}
        >
          {/* Layer stack */}
          <LayerStack
            highlightLayer={getHighlightLayer()}
            animationStyle="cascade"
          />

          {/* Description panel */}
          <div
            style={{
              maxWidth: 500,
              display: 'flex',
              flexDirection: 'column',
              gap: 30,
            }}
          >
            {/* Zone descriptions */}
            {highlightGateway ? (
              <div
                style={{
                  padding: 30,
                  backgroundColor: `${colors.gateway.L8}22`,
                  borderRadius: 16,
                  border: `2px solid ${colors.gateway.L8}`,
                }}
              >
                <div
                  style={{
                    fontSize: typography.fontSize.subheading,
                    color: colors.gateway.L8,
                    fontWeight: 700,
                    marginBottom: 16,
                  }}
                >
                  Layer 8: Neural Gateway
                </div>
                <div
                  style={{
                    fontSize: typography.fontSize.body,
                    color: colors.text.secondary,
                    lineHeight: 1.6,
                  }}
                >
                  The critical bridge between machine and mind. All BCI communication
                  passes through this layer—making it the prime target for security controls.
                </div>
              </div>
            ) : (
              <>
                <div
                  style={{
                    padding: 24,
                    backgroundColor: 'rgba(33, 150, 243, 0.1)',
                    borderRadius: 12,
                    borderLeft: `4px solid ${colors.silicon.L1}`,
                  }}
                >
                  <div
                    style={{
                      fontSize: typography.fontSize.body,
                      color: colors.silicon.L1,
                      fontWeight: 600,
                      marginBottom: 8,
                    }}
                  >
                    Silicon (L1-L7)
                  </div>
                  <div style={{ color: colors.text.secondary, fontSize: typography.fontSize.small }}>
                    Physical signals, protocols, and data transport
                  </div>
                </div>

                <div
                  style={{
                    padding: 24,
                    backgroundColor: 'rgba(76, 175, 80, 0.1)',
                    borderRadius: 12,
                    borderLeft: `4px solid ${colors.biology.L9}`,
                  }}
                >
                  <div
                    style={{
                      fontSize: typography.fontSize.body,
                      color: colors.biology.L9,
                      fontWeight: 600,
                      marginBottom: 8,
                    }}
                  >
                    Biology (L9-L14)
                  </div>
                  <div style={{ color: colors.text.secondary, fontSize: typography.fontSize.small }}>
                    Ion channels to cognition to identity
                  </div>
                </div>
              </>
            )}
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};
