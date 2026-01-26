import { Composition } from "remotion";
import { ONIDemoVideo } from "./ONIDemoVideo";
import { videoConfig } from "./data/oni-theme";

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
    </>
  );
};
