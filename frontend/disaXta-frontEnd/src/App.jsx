import {BrowserRouter, Routes, Route } from "react-router-dom";
import SharedLayout from "./components/ShareLayout";

function App() {
  return (
    <div>
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<SharedLayout/>}>

        </Route>
      </Routes>
      </BrowserRouter>
    </div>
   
  );
}

export default App;