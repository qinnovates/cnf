/**
 * AnimatedONILogo - Premium Apple-style logo animation
 * Features: Circular wave ripples, spring physics, dynamic color gradients
 */

import React, { useMemo } from 'react';
import { useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { colors } from '../data/oni-theme';

interface AnimatedONILogoProps {
  width?: number;
  height?: number;
  showText?: boolean;
}

// Seeded random for consistent wave positions
const seededRandom = (seed: number) => {
  const x = Math.sin(seed * 9999) * 10000;
  return x - Math.floor(x);
};

// Custom easing curve inspired by Apple's animations
const appleEaseOut = (t: number) => 1 - Math.pow(1 - t, 4);

export const AnimatedONILogo: React.FC<AnimatedONILogoProps> = ({
  width = 800,
  height = 800,
  showText = true,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const centerX = width / 2;
  const centerY = height / 2;

  // Main logo entrance - Apple-style spring
  const logoProgress = spring({
    frame,
    fps,
    config: { damping: 12, stiffness: 40, mass: 1.2 },
  });

  const logoScale = interpolate(
    Math.max(0, logoProgress),
    [0, 1],
    [0.3, 1],
    { easing: appleEaseOut }
  );

  const logoOpacity = interpolate(
    Math.max(0, logoProgress),
    [0, 0.3, 1],
    [0, 0.8, 1]
  );

  // Circular wave ripples configuration - purple-enhanced for curiosity/innovation
  const numWaves = 6;
  const waveColors = [
    colors.primary.accent,       // Cyan
    colors.primary.accentPurple, // Purple (curiosity)
    colors.primary.accent,       // Cyan
    colors.glow.purple,          // Purple
    colors.glow.blue,            // Blue-purple
    colors.primary.accentPurple, // Purple
  ];

  // Generate wave data
  const waves = useMemo(() => {
    return Array.from({ length: numWaves }, (_, i) => ({
      delay: i * 12,
      maxRadius: 300 + i * 60,
      thickness: 2 + (numWaves - i) * 0.5,
      color: waveColors[i % waveColors.length],
    }));
  }, []);

  // Rotating particle ring
  const numParticles = 24;
  const particles = useMemo(() => {
    return Array.from({ length: numParticles }, (_, i) => ({
      angle: (i / numParticles) * Math.PI * 2,
      radius: 180 + seededRandom(i * 1.5) * 40,
      size: 2 + seededRandom(i * 2.5) * 3,
      speed: 0.3 + seededRandom(i * 3.5) * 0.4,
      colorIndex: Math.floor(seededRandom(i * 4.5) * 4),
    }));
  }, []);

  const particleColors = [
    colors.primary.accent,
    colors.primary.accentPurple,
    colors.glow.purple,
    colors.glow.blue,
  ];

  // Glow pulse animation
  const glowPhase = Math.sin(frame * 0.04);
  const glowIntensity = interpolate(glowPhase, [-1, 1], [0.5, 1]);

  // Inner geometric pattern rotation
  const innerRotation = frame * 0.2;
  const outerRotation = frame * -0.1;

  // Text animation
  const textProgress = spring({
    frame: frame - 40,
    fps,
    config: { damping: 20, stiffness: 80 },
  });

  return (
    <div
      style={{
        width,
        height,
        position: 'relative',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      <svg
        width={width}
        height={height}
        viewBox={`0 0 ${width} ${height}`}
        style={{ position: 'absolute', top: 0, left: 0 }}
      >
        <defs>
          {/* Radial gradient for center glow */}
          <radialGradient id="centerGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor={colors.primary.accent} stopOpacity={0.4 * glowIntensity} />
            <stop offset="40%" stopColor={colors.primary.accent} stopOpacity={0.1 * glowIntensity} />
            <stop offset="100%" stopColor="transparent" stopOpacity={0} />
          </radialGradient>

          {/* Gradient for waves */}
          {waves.map((wave, i) => (
            <linearGradient
              key={`waveGrad-${i}`}
              id={`waveGradient-${i}`}
              x1="0%"
              y1="0%"
              x2="100%"
              y2="100%"
            >
              <stop offset="0%" stopColor={wave.color} stopOpacity={0.8} />
              <stop offset="50%" stopColor={colors.primary.accent} stopOpacity={0.6} />
              <stop offset="100%" stopColor={wave.color} stopOpacity={0.3} />
            </linearGradient>
          ))}

          {/* Glow filter */}
          <filter id="logoGlow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="8" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
          </filter>

          {/* Soft blur for waves */}
          <filter id="waveBlur" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="2" />
          </filter>
        </defs>

        {/* Background glow */}
        <circle
          cx={centerX}
          cy={centerY}
          r={250 * glowIntensity}
          fill="url(#centerGlow)"
          opacity={logoOpacity}
        />

        {/* Expanding circular waves */}
        {waves.map((wave, i) => {
          const waveFrame = Math.max(0, frame - wave.delay);
          const cycleDuration = 90; // frames per cycle
          const cycleProgress = (waveFrame % cycleDuration) / cycleDuration;

          // Apple-style ease out for wave expansion
          const easedProgress = appleEaseOut(cycleProgress);

          const waveRadius = interpolate(
            easedProgress,
            [0, 1],
            [60, wave.maxRadius]
          );

          const waveOpacity = interpolate(
            easedProgress,
            [0, 0.2, 0.7, 1],
            [0, 0.6, 0.4, 0]
          );

          // Only show after logo appears
          if (frame < 20 + wave.delay) return null;

          return (
            <circle
              key={`wave-${i}`}
              cx={centerX}
              cy={centerY}
              r={waveRadius}
              fill="none"
              stroke={`url(#waveGradient-${i})`}
              strokeWidth={wave.thickness}
              opacity={waveOpacity * logoOpacity}
              filter="url(#waveBlur)"
            />
          );
        })}

        {/* Rotating outer geometric ring */}
        <g
          style={{
            transform: `rotate(${outerRotation}deg)`,
            transformOrigin: `${centerX}px ${centerY}px`,
          }}
          opacity={logoOpacity * 0.3}
        >
          {[0, 1, 2, 3, 4, 5].map((i) => {
            const angle = (i / 6) * Math.PI * 2;
            const x1 = centerX + Math.cos(angle) * 280;
            const y1 = centerY + Math.sin(angle) * 280;
            const x2 = centerX + Math.cos(angle) * 320;
            const y2 = centerY + Math.sin(angle) * 320;

            return (
              <line
                key={`outer-line-${i}`}
                x1={x1}
                y1={y1}
                x2={x2}
                y2={y2}
                stroke={colors.primary.accent}
                strokeWidth={1}
                opacity={0.5}
              />
            );
          })}
        </g>

        {/* Inner rotating hexagon */}
        <g
          style={{
            transform: `rotate(${innerRotation}deg)`,
            transformOrigin: `${centerX}px ${centerY}px`,
          }}
          opacity={logoOpacity * 0.4}
        >
          <polygon
            points={Array.from({ length: 6 }, (_, i) => {
              const angle = (i / 6) * Math.PI * 2 - Math.PI / 2;
              const x = centerX + Math.cos(angle) * 200;
              const y = centerY + Math.sin(angle) * 200;
              return `${x},${y}`;
            }).join(' ')}
            fill="none"
            stroke={colors.gateway.L8}
            strokeWidth={1}
            strokeDasharray="10 20"
          />
        </g>

        {/* Orbiting particles */}
        {particles.map((particle, i) => {
          const orbitProgress = (frame * particle.speed * 0.01 + particle.angle) % (Math.PI * 2);
          const x = centerX + Math.cos(orbitProgress) * particle.radius;
          const y = centerY + Math.sin(orbitProgress) * particle.radius;

          // Fade in particles
          const particleOpacity = interpolate(
            frame - 30 - i * 2,
            [0, 20],
            [0, 0.8],
            { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }
          );

          // Pulse effect
          const pulse = 1 + Math.sin(frame * 0.1 + i) * 0.3;

          return (
            <circle
              key={`particle-${i}`}
              cx={x}
              cy={y}
              r={particle.size * pulse}
              fill={particleColors[particle.colorIndex]}
              opacity={particleOpacity * logoOpacity}
              filter="url(#logoGlow)"
            />
          );
        })}

        {/* Center connection lines to particles (select few) */}
        {particles.slice(0, 8).map((particle, i) => {
          const orbitProgress = (frame * particle.speed * 0.01 + particle.angle) % (Math.PI * 2);
          const x = centerX + Math.cos(orbitProgress) * particle.radius;
          const y = centerY + Math.sin(orbitProgress) * particle.radius;

          const lineOpacity = interpolate(
            Math.sin(frame * 0.05 + i),
            [-1, 1],
            [0.05, 0.15]
          );

          return (
            <line
              key={`connection-${i}`}
              x1={centerX}
              y1={centerY}
              x2={x}
              y2={y}
              stroke={particleColors[particle.colorIndex]}
              strokeWidth={0.5}
              opacity={lineOpacity * logoOpacity}
            />
          );
        })}
      </svg>

      {/* Main ONI Text Logo */}
      <div
        style={{
          position: 'relative',
          transform: `scale(${logoScale})`,
          opacity: logoOpacity,
          filter: `drop-shadow(0 0 ${30 * glowIntensity}px ${colors.primary.accent}66)`,
        }}
      >
        {/* ONI Letters */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: 8,
          }}
        >
          {['O', 'N', 'I'].map((letter, i) => {
            const letterProgress = spring({
              frame: frame - 10 - i * 8,
              fps,
              config: { damping: 10, stiffness: 100 },
            });

            const letterY = interpolate(
              Math.max(0, letterProgress),
              [0, 1],
              [40, 0]
            );

            const letterOpacity = Math.max(0, letterProgress);

            // Subtle color pulse per letter
            const letterGlow = interpolate(
              Math.sin(frame * 0.06 + i * 0.5),
              [-1, 1],
              [0.7, 1]
            );

            return (
              <span
                key={letter}
                style={{
                  fontSize: 140,
                  fontWeight: 800,
                  fontFamily: "'Inter', sans-serif",
                  letterSpacing: '-0.02em',
                  background: `linear-gradient(180deg,
                    ${colors.text.primary} 0%,
                    rgba(255,255,255,0.9) 40%,
                    ${colors.primary.accent}${Math.round(letterGlow * 100).toString(16).padStart(2, '0')} 100%
                  )`,
                  WebkitBackgroundClip: 'text',
                  WebkitTextFillColor: 'transparent',
                  transform: `translateY(${letterY}px)`,
                  opacity: letterOpacity,
                  display: 'inline-block',
                }}
              >
                {letter}
              </span>
            );
          })}
        </div>

        {/* Tagline */}
        {showText && (
          <div
            style={{
              marginTop: 20,
              textAlign: 'center',
              opacity: Math.max(0, textProgress),
              transform: `translateY(${interpolate(
                Math.max(0, textProgress),
                [0, 1],
                [20, 0]
              )}px)`,
            }}
          >
            <div
              style={{
                fontSize: 24,
                fontWeight: 300,
                letterSpacing: '0.3em',
                color: colors.primary.accent,
                textTransform: 'uppercase',
              }}
            >
              Open Neural Interface
            </div>
            <div
              style={{
                fontSize: 16,
                fontWeight: 400,
                letterSpacing: '0.1em',
                color: colors.text.muted,
                marginTop: 8,
              }}
            >
              The OSI of Mind
            </div>
          </div>
        )}
      </div>

      {/* Outer pulsing ring */}
      <div
        style={{
          position: 'absolute',
          width: 500,
          height: 500,
          borderRadius: '50%',
          border: `1px solid ${colors.primary.accent}`,
          opacity: interpolate(
            Math.sin(frame * 0.03),
            [-1, 1],
            [0.1, 0.3]
          ) * logoOpacity,
          transform: `scale(${1 + Math.sin(frame * 0.02) * 0.05})`,
        }}
      />

      {/* Second pulsing ring (offset phase) */}
      <div
        style={{
          position: 'absolute',
          width: 600,
          height: 600,
          borderRadius: '50%',
          border: `1px solid ${colors.gateway.L8}`,
          opacity: interpolate(
            Math.sin(frame * 0.025 + Math.PI),
            [-1, 1],
            [0.05, 0.2]
          ) * logoOpacity,
          transform: `scale(${1 + Math.sin(frame * 0.015 + 1) * 0.03})`,
        }}
      />
    </div>
  );
};

// Standalone circular wave component for backgrounds
export const CircularWaves: React.FC<{
  width?: number;
  height?: number;
  numWaves?: number;
  baseRadius?: number;
  color?: string;
}> = ({
  width = 1920,
  height = 1080,
  numWaves = 5,
  baseRadius = 100,
  color = colors.primary.accent,
}) => {
  const frame = useCurrentFrame();
  const centerX = width / 2;
  const centerY = height / 2;

  return (
    <svg width={width} height={height} style={{ position: 'absolute' }}>
      <defs>
        <filter id="circularWaveBlur">
          <feGaussianBlur stdDeviation="3" />
        </filter>
      </defs>

      {Array.from({ length: numWaves }, (_, i) => {
        const delay = i * 20;
        const waveFrame = Math.max(0, frame - delay);
        const cycleDuration = 120;
        const progress = (waveFrame % cycleDuration) / cycleDuration;
        const easedProgress = appleEaseOut(progress);

        const maxRadius = Math.max(width, height) * 0.8;
        const radius = interpolate(easedProgress, [0, 1], [baseRadius, maxRadius]);
        const opacity = interpolate(easedProgress, [0, 0.1, 0.6, 1], [0, 0.4, 0.2, 0]);

        return (
          <circle
            key={i}
            cx={centerX}
            cy={centerY}
            r={radius}
            fill="none"
            stroke={color}
            strokeWidth={2}
            opacity={opacity}
            filter="url(#circularWaveBlur)"
          />
        );
      })}
    </svg>
  );
};

export default AnimatedONILogo;
