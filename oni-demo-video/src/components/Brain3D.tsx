/**
 * Brain3D - 3D neural network visualization
 * Uses React Three Fiber for Apple-quality 3D rendering
 */

import React, { useMemo, useRef } from 'react';
import { ThreeCanvas } from '@remotion/three';
import { useCurrentFrame, useVideoConfig, interpolate, spring } from 'remotion';
import * as THREE from 'three';
import { colors } from '../data/oni-theme';

// Neural node component
const NeuralNode: React.FC<{
  position: [number, number, number];
  size?: number;
  color?: string;
  pulseOffset?: number;
}> = ({ position, size = 0.1, color = '#00e5ff', pulseOffset = 0 }) => {
  const frame = useCurrentFrame();

  // Pulse animation
  const pulse = Math.sin((frame + pulseOffset) * 0.1) * 0.3 + 1;
  const glowIntensity = interpolate(Math.sin((frame + pulseOffset) * 0.15), [-1, 1], [0.5, 1]);

  return (
    <mesh position={position} scale={[pulse * size, pulse * size, pulse * size]}>
      <sphereGeometry args={[1, 16, 16]} />
      <meshStandardMaterial
        color={color}
        emissive={color}
        emissiveIntensity={glowIntensity}
        transparent
        opacity={0.9}
      />
    </mesh>
  );
};

// Connection as a thin cylinder between nodes
const NeuralConnection: React.FC<{
  start: [number, number, number];
  end: [number, number, number];
  color?: string;
  pulseOffset?: number;
}> = ({ start, end, color = '#00e5ff', pulseOffset = 0 }) => {
  const frame = useCurrentFrame();

  // Calculate cylinder orientation and length
  const startVec = new THREE.Vector3(...start);
  const endVec = new THREE.Vector3(...end);
  const midpoint = startVec.clone().add(endVec).multiplyScalar(0.5);
  const length = startVec.distanceTo(endVec);
  const direction = endVec.clone().sub(startVec).normalize();

  // Create rotation quaternion
  const quaternion = new THREE.Quaternion();
  quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), direction);

  // Traveling pulse effect
  const pulseProgress = ((frame + pulseOffset) * 0.03) % 1;
  const pulsePosition = startVec.clone().lerp(endVec, pulseProgress);

  return (
    <group>
      {/* Connection line as thin cylinder */}
      <mesh position={[midpoint.x, midpoint.y, midpoint.z]} quaternion={quaternion}>
        <cylinderGeometry args={[0.01, 0.01, length, 8]} />
        <meshBasicMaterial color={color} transparent opacity={0.3} />
      </mesh>
      {/* Traveling pulse */}
      <mesh position={[pulsePosition.x, pulsePosition.y, pulsePosition.z]}>
        <sphereGeometry args={[0.03, 8, 8]} />
        <meshBasicMaterial color={color} transparent opacity={0.8} />
      </mesh>
    </group>
  );
};

// Main brain visualization
const BrainVisualization: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const groupRef = useRef<THREE.Group>(null);

  // Generate neural network nodes (use seeded random for consistency)
  const nodes = useMemo(() => {
    const nodeList: { position: [number, number, number]; layer: number }[] = [];

    // Simple seeded random
    const seededRandom = (seed: number) => {
      const x = Math.sin(seed) * 10000;
      return x - Math.floor(x);
    };

    // Create layers of nodes (like brain regions)
    const layers = [
      { count: 8, radius: 1.5, y: 0.8 },
      { count: 12, radius: 1.8, y: 0.3 },
      { count: 12, radius: 2.0, y: -0.2 },
      { count: 8, radius: 1.5, y: -0.7 },
    ];

    let seed = 1;
    layers.forEach((layer, layerIndex) => {
      for (let i = 0; i < layer.count; i++) {
        const angle = (i / layer.count) * Math.PI * 2;
        const x = Math.cos(angle) * layer.radius + (seededRandom(seed++) - 0.5) * 0.3;
        const z = Math.sin(angle) * layer.radius + (seededRandom(seed++) - 0.5) * 0.3;
        const y = layer.y + (seededRandom(seed++) - 0.5) * 0.2;
        nodeList.push({ position: [x, y, z], layer: layerIndex });
      }
    });

    return nodeList;
  }, []);

  // Generate connections between nearby nodes
  const connections = useMemo(() => {
    const conns: { start: [number, number, number]; end: [number, number, number] }[] = [];
    let seed = 100;

    const seededRandom = (s: number) => {
      const x = Math.sin(s) * 10000;
      return x - Math.floor(x);
    };

    nodes.forEach((node, i) => {
      nodes.forEach((other, j) => {
        if (i >= j) return;
        const dist = Math.sqrt(
          Math.pow(node.position[0] - other.position[0], 2) +
          Math.pow(node.position[1] - other.position[1], 2) +
          Math.pow(node.position[2] - other.position[2], 2)
        );
        if (dist < 1.2 && seededRandom(seed++) > 0.5) {
          conns.push({ start: node.position, end: other.position });
        }
      });
    });

    return conns;
  }, [nodes]);

  // Rotation animation
  const rotation = frame * 0.005;

  // Scale animation with spring
  const scaleSpring = spring({
    frame,
    fps,
    config: { damping: 100, stiffness: 50 },
  });

  // Get layer color
  const getLayerColor = (layer: number) => {
    const layerColors = [
      colors.biology.L14,
      colors.biology.L11,
      colors.gateway.L8,
      colors.silicon.L3,
    ];
    return layerColors[layer] || colors.primary.accent;
  };

  return (
    <group ref={groupRef} rotation={[0.2, rotation, 0]} scale={scaleSpring}>
      {/* Ambient glow sphere */}
      <mesh>
        <sphereGeometry args={[2.5, 32, 32]} />
        <meshBasicMaterial
          color={colors.primary.accent}
          transparent
          opacity={0.05}
          side={THREE.BackSide}
        />
      </mesh>

      {/* Neural connections */}
      {connections.map((conn, i) => (
        <NeuralConnection
          key={`conn-${i}`}
          start={conn.start}
          end={conn.end}
          color={colors.primary.accent}
          pulseOffset={i * 10}
        />
      ))}

      {/* Neural nodes */}
      {nodes.map((node, i) => (
        <NeuralNode
          key={`node-${i}`}
          position={node.position}
          size={0.08}
          color={getLayerColor(node.layer)}
          pulseOffset={i * 5}
        />
      ))}
    </group>
  );
};

// Export the full 3D brain component
export const Brain3D: React.FC<{
  width?: number;
  height?: number;
}> = ({ width = 600, height = 600 }) => {
  return (
    <ThreeCanvas
      width={width}
      height={height}
      camera={{ position: [0, 0, 5], fov: 50 }}
      style={{ background: 'transparent' }}
    >
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} intensity={1} />
      <pointLight position={[-10, -10, -10]} intensity={0.5} color="#00e5ff" />
      <BrainVisualization />
    </ThreeCanvas>
  );
};
