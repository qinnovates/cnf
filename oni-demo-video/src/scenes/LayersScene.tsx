/**
 * Layers Scene - 14-layer ONI model visualization
 * Shows hourglass image first, then transitions to animated layer stack
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, spring, useVideoConfig, Img, staticFile, interpolate } from 'remotion';
import { LayerStack } from '../components/LayerStack';
import { FloatingParticles } from '../components/Particles';
import { colors } from '../data/oni-theme';

export const LayersScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Phase 1: Show hourglass image (frames 0-300)
  // Phase 2: Show animated layer stack (frames 300+)
  const showHourglass = frame < 300;
  const showStack = frame >= 300;

  // Hourglass image animation
  const hourglassProgress = spring({
    frame,
    fps,
    config: { damping: 25, stiffness: 60 },
  });

  const hourglassOpacity = interpolate(
    frame,
    [0, 30, 260, 300],
    [0, 1, 1, 0],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
  );

  const hourglassScale = interpolate(
    Math.max(0, hourglassProgress),
    [0, 1],
    [0.92, 1]
  );

  // Stack animation
  const stackProgress = spring({
    frame: frame - 300,
    fps,
    config: { damping: 25, stiffness: 80 },
  });

  // Subtle glow pulse
  const glowIntensity = interpolate(
    Math.sin(frame * 0.04),
    [-1, 1],
    [0.2, 0.5]
  );

  // Highlight specific layers based on timing
  const getHighlightLayer = () => {
    if (frame >= 600 && frame < 750) return 8; // Gateway
    if (frame >= 750 && frame < 850) return 14; // Identity
    if (frame >= 850 && frame < 950) return 1; // Physical
    return undefined;
  };

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at center, ${colors.primary.main} 0%, ${colors.primary.dark} 80%)`,
      }}
    >
      {/* Subtle particles */}
      <FloatingParticles
        count={30}
        color={showStack ? colors.gateway.L8 : colors.primary.accent}
        speed={0.1}
        minSize={1}
        maxSize={2}
      />

      {/* Phase 1: Centered hourglass image */}
      {showHourglass && (
        <div
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: `translate(-50%, -50%) scale(${hourglassScale})`,
            opacity: hourglassOpacity,
            filter: `drop-shadow(0 0 ${40 * glowIntensity}px ${colors.primary.accent}33)`,
          }}
        >
          <Img
            src={staticFile('assets/ONI_Layers_Diagram-HOURGLASS.png')}
            style={{
              maxWidth: '80vw',
              maxHeight: '80vh',
              objectFit: 'contain',
            }}
          />
        </div>
      )}

      {/* Phase 2: Animated layer stack */}
      {showStack && (
        <div
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            opacity: Math.max(0, stackProgress),
          }}
        >
          <LayerStack
            highlightLayer={getHighlightLayer()}
            animationStyle="cascade"
          />
        </div>
      )}

      {/* Subtle vignette */}
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          background: 'radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.3) 100%)',
          pointerEvents: 'none',
        }}
      />

      {/* Bottom gradient fade */}
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          right: 0,
          height: 100,
          background: `linear-gradient(transparent, ${colors.primary.dark}88)`,
          pointerEvents: 'none',
        }}
      />
    </AbsoluteFill>
  );
};
