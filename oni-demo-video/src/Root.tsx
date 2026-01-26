import { Composition } from "remotion";
import { ONIDemoVideo } from "./ONIDemoVideo";
import { videoConfig } from "./data/oni-theme";
import { LayersCanvasScene } from "./scenes/LayersCanvasScene";
import { TitleSceneEnhanced } from "./scenes/TitleSceneEnhanced";
import { TitleThreadsScene } from "./scenes/TitleThreadsScene";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="ONIDemoVideo"
        component={ONIDemoVideo}
        durationInFrames={videoConfig.durationInFrames}
        fps={videoConfig.fps}
        width={videoConfig.width}
        height={videoConfig.height}
      />
      {/* Preview composition for development - shorter version */}
      <Composition
        id="ONIDemoPreview"
        component={ONIDemoVideo}
        durationInFrames={900} // 30 seconds preview
        fps={videoConfig.fps}
        width={videoConfig.width}
        height={videoConfig.height}
      />
      {/* Canvas-based Layers Scene */}
      <Composition
        id="LayersCanvas"
        component={LayersCanvasScene}
        durationInFrames={300} // 10 seconds
        fps={videoConfig.fps}
        width={videoConfig.width}
        height={videoConfig.height}
      />
      {/* Enhanced Title with React Bits + Canvas - BEST OF ALL WORLDS */}
      <Composition
        id="TitleEnhanced"
        component={TitleSceneEnhanced}
        durationInFrames={240} // 8 seconds
        fps={videoConfig.fps}
        width={videoConfig.width}
        height={videoConfig.height}
      />
      {/* Title with Threads - Brain Wave Animation */}
      <Composition
        id="TitleThreads"
        component={TitleThreadsScene}
        durationInFrames={240} // 8 seconds
        fps={videoConfig.fps}
        width={videoConfig.width}
        height={videoConfig.height}
      />
    </>
  );
};
