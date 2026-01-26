/**
 * Title Scene - Apple-level restraint
 * Pure. Minimal. Confident.
 *
 * Design system:
 * - Base unit: 180px (ONI type size)
 * - Spacing: 180 × 0.3 = 54px
 * - Tagline: 180 ÷ 5 = 36px (5:1 ratio)
 * - Line: 2px weight, 120px wide (type height × 0.67)
 */

import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';

export const TitleScene: React.FC = () => {
  const frame = useCurrentFrame();

  // Apple's signature ease - glacial, inevitable
  const appleEase = (t: number) => {
    // Quart ease-out: slow start, graceful settle
    return 1 - Math.pow(1 - t, 4);
  };

  // === TIMING (at 30fps) ===
  // ONI: 0-120 frames (4 seconds) - the hero moment
  // Hold: 120-160 frames (1.3 seconds) - let it breathe
  // Line: 160-220 frames (2 seconds) - deliberate draw
  // Tagline: 200-260 frames (2 seconds, slight overlap)

  // ONI fade - 4 seconds, from void
  const oniRaw = interpolate(frame, [0, 120], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const oniOpacity = appleEase(oniRaw);
  const oniY = interpolate(oniOpacity, [0, 1], [30, 0]);

  // Line draw - after the hold
  const lineRaw = interpolate(frame, [160, 220], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const lineProgress = appleEase(lineRaw);

  // Tagline - overlaps slightly with line finish
  const taglineRaw = interpolate(frame, [200, 260], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const taglineOpacity = appleEase(taglineRaw);
  const taglineY = interpolate(taglineOpacity, [0, 1], [16, 0]);

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#000000',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      {/* ONI - The mark. Nothing else. */}
      <div
        style={{
          fontSize: 180,
          fontWeight: 500,
          fontFamily: "'SF Pro Display', -apple-system, 'Helvetica Neue', sans-serif",
          letterSpacing: '0.12em',
          color: '#ffffff',
          opacity: oniOpacity,
          transform: `translateY(${oniY}px)`,
        }}
      >
        ONI
      </div>

      {/* Thin line - 2px, draws from center */}
      <div
        style={{
          width: 120,
          height: 2,
          backgroundColor: '#ffffff',
          marginTop: 54,
          marginBottom: 54,
          opacity: lineProgress,
          transform: `scaleX(${lineProgress})`,
          transformOrigin: 'center',
        }}
      />

      {/* Tagline - one statement */}
      <div
        style={{
          fontSize: 36,
          fontWeight: 300,
          fontFamily: "'SF Pro Display', -apple-system, 'Helvetica Neue', sans-serif",
          letterSpacing: '0.02em',
          color: '#ffffff',
          opacity: taglineOpacity,
          transform: `translateY(${taglineY}px)`,
        }}
      >
        The mind is the last frontier worth protecting.
      </div>
    </AbsoluteFill>
  );
};
