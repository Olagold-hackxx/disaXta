import { BrowserRouter, Routes, Route } from "react-router-dom";
import SharedLayout from "./components/ShareLayout";
import Mainfeed from "./components/Mainfeed";
import Community from "./components/Community";
import Education from "./components/Education";
import Happeningnow from "./components/Happeningnow";
import WaverX from "./components/WaverX";
import Profile from "./components/Profile";
import Comment from "./pages/Comment";
import Createpost from "./components/Createpost";
import Createcomment from "./components/Createcomment";
import Waverx from "./pages/Waverx";
import Signuppage from "./pages/Signuppage";
import Emailconfirmation from "./pages/Emailconfirmation";
import Loginpage from "./pages/LoginPage";

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<SharedLayout />}>
            <Route index element={<Mainfeed />} />
            <Route path="/community" element={<Community />} />
            <Route path="/education" element={<Education />} />
            <Route path="/happeningnow" element={<Happeningnow />} />
            <Route path="/waverx-tweet" element={<WaverX />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/:postId/comments" element={<Comment />} />
            <Route path="/createpost" element={<Createpost />} />
            <Route path="/:postId/comment" element={<Createcomment />} />
          </Route>

          <Route path="/:userId/waverx" element={<Waverx />} />
          <Route path="/signup" element={<Signuppage />} />
          <Route
            path="/emailconfirmation/:userToken"
            element={<Emailconfirmation />}
          />
          <Route path="/login" element={<Loginpage />} />
          {/* <Route path="/forgotpassword" element={<Forgotpasswordpage />} /> */}
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
