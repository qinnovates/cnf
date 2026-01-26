import { Composition } from "remotion";
import { ONIDemoVideo } from "./ONIDemoVideo";
import { videoConfig } from "./data/oni-theme";
import { TitleVectorScene } from "./scenes/TitleVectorScene";

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
      {/* Title Scene - Vector Waves */}
      <Composition
        id="TitleVector"
        component={TitleVectorScene}
        durationInFrames={300}
        fps={videoConfig.fps}
        width={videoConfig.width}
        height={videoConfig.height}
      />
    </>
  );
};
