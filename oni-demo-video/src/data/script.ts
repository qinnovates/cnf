/**
 * ONI Framework Demo Video Script
 * ~400 words, 3:30 runtime
 *
 * For ElevenLabs generation, use voice: "Adam" (authoritative) or "Rachel" (professional)
 * Request word-level timestamps for precise sync
 */

export interface ScriptLine {
  text: string;
  startFrame: number;
  endFrame: number;
  scene: string;
}

export const script: ScriptLine[] = [
  // Scene 0: Cold Open (0:00-0:08)
  {
    scene: 'coldOpen',
    text: "Brain-computer interfaces are no longer science fiction.",
    startFrame: 0,
    endFrame: 120,
  },
  {
    scene: 'coldOpen',
    text: "They're in operating rooms. They're in research labs. They're coming to consumers.",
    startFrame: 120,
    endFrame: 240,
  },

  // Scene 1: Title (0:08-0:15)
  {
    scene: 'title',
    text: "But who's protecting the most sensitive data in existence?",
    startFrame: 240,
    endFrame: 360,
  },
  {
    scene: 'title',
    text: "Your thoughts.",
    startFrame: 360,
    endFrame: 450,
  },

  // Scene 2: Problem (0:15-0:40)
  {
    scene: 'problem',
    text: "Today's brain-computer interfaces lack standardized security frameworks.",
    startFrame: 450,
    endFrame: 570,
  },
  {
    scene: 'problem',
    text: "There's no OSI model for neural interfaces.",
    startFrame: 570,
    endFrame: 690,
  },
  {
    scene: 'problem',
    text: "No common language between neuroscientists, engineers, and security researchers.",
    startFrame: 690,
    endFrame: 870,
  },
  {
    scene: 'problem',
    text: "Until now.",
    startFrame: 870,
    endFrame: 960,
  },
  {
    scene: 'problem',
    text: "Introducing the Open Neural Interface Framework.",
    startFrame: 960,
    endFrame: 1200,
  },

  // Scene 3: 14-Layer Model (0:40-1:20)
  {
    scene: 'layers',
    text: "ONI defines fourteen layers spanning silicon to synapse.",
    startFrame: 1200,
    endFrame: 1380,
  },
  {
    scene: 'layers',
    text: "Layers one through seven handle the silicon side—physical signals, protocols, and data transport.",
    startFrame: 1380,
    endFrame: 1620,
  },
  {
    scene: 'layers',
    text: "Layer eight is the Neural Gateway—the critical bridge between machine and mind.",
    startFrame: 1620,
    endFrame: 1860,
  },
  {
    scene: 'layers',
    text: "Layers nine through fourteen map biological processing—from ion channels to cognition to identity.",
    startFrame: 1860,
    endFrame: 2100,
  },
  {
    scene: 'layers',
    text: "Each layer has defined security controls, threat models, and verification methods.",
    startFrame: 2100,
    endFrame: 2400,
  },

  // Scene 4: Coherence Metric (1:20-1:50)
  {
    scene: 'coherence',
    text: "But how do you measure neural security?",
    startFrame: 2400,
    endFrame: 2520,
  },
  {
    scene: 'coherence',
    text: "ONI introduces the Coherence Score—a unified metric combining phase synchronization, timing precision, and frequency response.",
    startFrame: 2520,
    endFrame: 2820,
  },
  {
    scene: 'coherence',
    text: "It's not a black box. It's fully configurable and mathematically grounded.",
    startFrame: 2820,
    endFrame: 3060,
  },
  {
    scene: 'coherence',
    text: "Explore it yourself in our interactive playground.",
    startFrame: 3060,
    endFrame: 3300,
  },

  // Scene 5: TARA Platform (1:50-2:25)
  {
    scene: 'tara',
    text: "For security professionals, there's TARA—the Telemetry Analysis & Response Automation platform.",
    startFrame: 3300,
    endFrame: 3540,
  },
  {
    scene: 'tara',
    text: "Real-time brain topology visualization.",
    startFrame: 3540,
    endFrame: 3690,
  },
  {
    scene: 'tara',
    text: "Attack simulation across all fourteen layers.",
    startFrame: 3690,
    endFrame: 3870,
  },
  {
    scene: 'tara',
    text: "Neural Signal Assurance Monitoring that flags anomalies before they become breaches.",
    startFrame: 3870,
    endFrame: 4140,
  },
  {
    scene: 'tara',
    text: "All open source. All verifiable.",
    startFrame: 4140,
    endFrame: 4350,
  },

  // Scene 6: Academic Foundation (2:25-2:50)
  {
    scene: 'academic',
    text: "ONI isn't built in a vacuum.",
    startFrame: 4350,
    endFrame: 4470,
  },
  {
    scene: 'academic',
    text: "It extends the threat models of Kohno and colleagues at the University of Washington.",
    startFrame: 4470,
    endFrame: 4710,
  },
  {
    scene: 'academic',
    text: "It incorporates neurosecurity research from Columbia, Yale, and the Graz BCI Lab.",
    startFrame: 4710,
    endFrame: 4980,
  },
  {
    scene: 'academic',
    text: "Every claim is cited. Every formula is documented.",
    startFrame: 4980,
    endFrame: 5070,
  },
  {
    scene: 'academic',
    text: "Built for researchers, developers, regulators, security teams...",
    startFrame: 5070,
    endFrame: 5220,
  },
  {
    scene: 'academic',
    text: "...and you.",
    startFrame: 5220,
    endFrame: 5340,
  },

  // Scene 7: Call to Action (2:53-3:15)
  {
    scene: 'cta',
    text: "Ready to secure the neural frontier?",
    startFrame: 5340,
    endFrame: 5460,
  },
  {
    scene: 'cta',
    text: "Install ONI with a single command.",
    startFrame: 5460,
    endFrame: 5580,
  },
  {
    scene: 'cta',
    text: "pip install oni-framework",
    startFrame: 5580,
    endFrame: 5700,
  },
  {
    scene: 'cta',
    text: "Explore the documentation on GitHub.",
    startFrame: 5700,
    endFrame: 5820,
  },
  {
    scene: 'cta',
    text: "Join us in building the security standards for brain-computer interfaces.",
    startFrame: 5820,
    endFrame: 5970,
  },

  // Scene 8: Credits (3:19-3:30)
  {
    scene: 'credits',
    text: "The Open Neural Interface Framework.",
    startFrame: 5970,
    endFrame: 6090,
  },
  {
    scene: 'credits',
    text: "The OSI of Mind.",
    startFrame: 6090,
    endFrame: 6210,
  },
];

// Full script as single text for voiceover generation
export const fullScript = script.map(line => line.text).join(' ');

// Word count: ~380 words
// Estimated read time at 110 WPM: ~3:27 (fits 3:30 with brief pauses)
// Final frame: 6210 = 3:27 at 30fps
