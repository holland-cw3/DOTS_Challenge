import { TransformWrapper, TransformComponent } from "react-zoom-pan-pinch";

import "./App.css";
import map from './map.png'







function App() {
  return (
    <div>

      <div class=''>
        
      </div>
      <TransformWrapper>
        <TransformComponent>
          <img src={map} alt="test" />
        </TransformComponent>
      </TransformWrapper>
      </div>

  );
}

export default App;
