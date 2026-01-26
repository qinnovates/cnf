/**
 * Threads - Inspired by React Bits
 * Soft glowing waves that move like silk - resembling brain waves
 * Based on: https://medium.com/@ravi-pai/rebuilt-reactbits-threads-animation-in-flutter
 */

import React, { useRef, useEffect } from 'react';
import { useCurrentFrame, useVideoConfig, interpolate } from 'remotion';

interface ThreadsProps {
  color?: string;
  secondaryColor?: string;
  lineCount?: number;
  amplitude?: number;
  speed?: number;
  frequency?: number;
  blur?: number;
  opacity?: number;
}

export const Threads: React.FC<ThreadsProps> = ({
  color = '#00e5ff',
  secondaryColor = '#a855f7',
  lineCount = 20,
  amplitude = 80,
  speed = 1,
  frequency = 1,
  blur = 2,
  opacity = 0.6,
}) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const frame = useCurrentFrame();
  const { width, height, fps } = useVideoConfig();

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.clearRect(0, 0, width, height);

    const time = (frame / fps) * speed;
    const points = 200; // Resolution of each wave
    const centerY = height / 2;

    // Fade in
    const fadeIn = interpolate(frame, [0, 30], [0, 1], {
      extrapolateRight: 'clamp',
    });

    // Draw each thread line
    for (let line = 0; line < lineCount; line++) {
      const lineProgress = line / lineCount;

      // Vertical offset for each line (spread across screen)
      const yOffset = (lineProgress - 0.5) * height * 0.8;

      // Each line has slightly different parameters for organic feel
      const lineFreq = frequency * (0.8 + lineProgress * 0.4);
      const lineSpeed = speed * (0.7 + lineProgress * 0.6);
      const lineAmp = amplitude * (0.6 + Math.sin(lineProgress * Math.PI) * 0.8);

      // Phase offset for each line
      const phaseOffset = line * 0.3;

      ctx.beginPath();

      for (let i = 0; i <= points; i++) {
        const x = (i / points) * width;
        const xNorm = i / points; // 0 to 1

        // Primary wave - smooth and wide
        const wave1 = Math.sin((xNorm * lineFreq + time * lineSpeed + phaseOffset) * Math.PI * 2);

        // Secondary wave - faster and smaller (adds complexity)
        const wave2 = Math.sin((xNorm * lineFreq * 2.5 + time * lineSpeed * 1.5 + phaseOffset) * Math.PI * 2) * 0.3;

        // Tertiary wave - subtle high frequency detail
        const wave3 = Math.sin((xNorm * lineFreq * 5 + time * lineSpeed * 0.7) * Math.PI * 2) * 0.1;

        // Combine waves
        const combinedWave = wave1 + wave2 + wave3;

        // Edge fade - waves fade at edges
        const edgeFade = Math.sin(xNorm * Math.PI);

        const y = centerY + yOffset + combinedWave * lineAmp * edgeFade;

        if (i === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }

      // Gradient color based on line position
      const gradient = ctx.createLinearGradient(0, 0, width, 0);
      const mixRatio = lineProgress;

      // Interpolate between primary and secondary color
      gradient.addColorStop(0, `${color}00`);
      gradient.addColorStop(0.2, mixRatio < 0.5 ? color : secondaryColor);
      gradient.addColorStop(0.5, mixRatio < 0.5 ? secondaryColor : color);
      gradient.addColorStop(0.8, mixRatio < 0.5 ? color : secondaryColor);
      gradient.addColorStop(1, `${secondaryColor}00`);

      ctx.strokeStyle = gradient;
      ctx.lineWidth = 2 + Math.sin(lineProgress * Math.PI) * 2;
      ctx.lineCap = 'round';
      ctx.globalAlpha = opacity * fadeIn * (0.3 + Math.sin(lineProgress * Math.PI) * 0.7);

      // Apply blur via shadow
      ctx.shadowColor = mixRatio < 0.5 ? color : secondaryColor;
      ctx.shadowBlur = blur + Math.sin(lineProgress * Math.PI) * blur;

      ctx.stroke();
    }

    // Reset
    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;

  }, [frame, width, height, fps, color, secondaryColor, lineCount, amplitude, speed, frequency, blur, opacity]);

  return (
    <canvas
      ref={canvasRef}
      width={width}
      height={height}
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
      }}
    />
  );
};

export default Threads;
