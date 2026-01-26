/**
 * ONI Framework Design System
 * Color palette and theme constants for the demo video
 */

export const colors = {
  // Primary palette - matches ONI branding
  primary: {
    dark: '#0a0e1a',      // Deep navy background
    main: '#1a237e',      // ONI navy blue
    light: '#3949ab',     // Lighter blue for highlights
    accent: '#00e5ff',    // Cyan accent (neural glow)
  },

  // Layer colors - 14-layer model
  silicon: {
    L1: '#2196f3',  // Physical Carrier - blue
    L2: '#1e88e5',  // Signal Processing
    L3: '#1976d2',  // Protocol
    L4: '#1565c0',  // Transport
    L5: '#0d47a1',  // Session
    L6: '#0277bd',  // Presentation
    L7: '#01579b',  // Application Interface
  },

  gateway: {
    L8: '#ff9800',  // Neural Gateway - orange (bridge)
  },

  biology: {
    L9:  '#4caf50',  // Ion Channel Encoding - green
    L10: '#43a047',  // Spike Train
    L11: '#388e3c',  // Neural Population
    L12: '#2e7d32',  // Circuit Dynamics
    L13: '#1b5e20',  // Cognitive Function
    L14: '#4a148c',  // Identity & Ethics - purple
  },

  // Security states
  security: {
    safe: '#00c853',
    warning: '#ffc107',
    danger: '#f44336',
    blocked: '#ff1744',
  },

  // Text colors
  text: {
    primary: '#ffffff',
    secondary: 'rgba(255, 255, 255, 0.7)',
    muted: 'rgba(255, 255, 255, 0.5)',
  },

  // Gradients
  gradients: {
    title: 'linear-gradient(135deg, #1a237e 0%, #0d47a1 50%, #00e5ff 100%)',
    silicon: 'linear-gradient(180deg, #2196f3 0%, #01579b 100%)',
    biology: 'linear-gradient(180deg, #4caf50 0%, #1b5e20 100%)',
    gateway: 'linear-gradient(180deg, #ff9800 0%, #e65100 100%)',
  },
};

export const typography = {
  fontFamily: {
    heading: "'Inter', 'Segoe UI', sans-serif",
    body: "'Inter', 'Segoe UI', sans-serif",
    mono: "'Fira Code', 'Consolas', monospace",
  },
  fontSize: {
    title: 72,
    subtitle: 36,
    heading: 48,
    subheading: 32,
    body: 24,
    small: 18,
    formula: 28,
  },
};

export const spacing = {
  xs: 8,
  sm: 16,
  md: 24,
  lg: 32,
  xl: 48,
  xxl: 64,
};

export const animation = {
  // Spring configs
  spring: {
    gentle: { mass: 1, damping: 20, stiffness: 100 },
    bouncy: { mass: 1, damping: 15, stiffness: 150 },
    stiff: { mass: 1, damping: 25, stiffness: 200 },
  },
  // Timing in frames (30fps)
  timing: {
    fast: 10,
    medium: 20,
    slow: 30,
  },
};

// Video settings
export const videoConfig = {
  fps: 30,
  width: 1920,
  height: 1080,
  durationInSeconds: 210, // 3:30
  durationInFrames: 210 * 30, // 6300 frames
};

// Scene timestamps (in frames at 30fps)
export const sceneTimestamps = {
  coldOpen: { start: 0, end: 8 * 30 },           // 0:00-0:08 (240 frames)
  title: { start: 8 * 30, end: 15 * 30 },         // 0:08-0:15 (210 frames)
  problem: { start: 15 * 30, end: 40 * 30 },      // 0:15-0:40 (750 frames)
  layers: { start: 40 * 30, end: 80 * 30 },       // 0:40-1:20 (1200 frames)
  coherence: { start: 80 * 30, end: 110 * 30 },   // 1:20-1:50 (900 frames)
  tara: { start: 110 * 30, end: 145 * 30 },       // 1:50-2:25 (1050 frames)
  academic: { start: 145 * 30, end: 170 * 30 },   // 2:25-2:50 (750 frames)
  cta: { start: 170 * 30, end: 195 * 30 },        // 2:50-3:15 (750 frames)
  credits: { start: 195 * 30, end: 210 * 30 },    // 3:15-3:30 (450 frames)
};
