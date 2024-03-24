//import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import SharedLayout from "./components/ShareLayout";
import Mainfeed from "./components/Mainfeed";
import Community from "./components/Community";
import Education from "./components/Education";
import Happeningnow from "./components/Happeningnow";
import DisaX from "./components/DisaX";
import Profile from "./components/Profile";
import Comment from "./pages/Comment";
import Createpost from "./components/Createpost";
import Createcomment from "./components/Createcomment";
import DisaXBot from "./pages/DisaX";
import Signuppage from "./pages/Signuppage";
import Emailconfirmation from "./pages/Emailconfirmation";
import Loginpage from "./pages/LoginPage";
import Forgotpasswordpage from "./pages/Forgotpasswordpage";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function App() {
  return (
    <div>
      <ToastContainer />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<SharedLayout />}>
            <Route index element={<Mainfeed />} />
            <Route path="/community" element={<Community />} />
            <Route path="/education" element={<Education />} />
            <Route path="/happeningnow" element={<Happeningnow />} />
            <Route path="/disaX" element={<DisaX />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/:postId/comments" element={<Comment />} />
            <Route path="/createpost" element={<Createpost />} />
            <Route path="/:postId/comment" element={<Createcomment />} />
          </Route>

          <Route path="/:userId/disaX" element={<DisaXBot />} />
          <Route path="/signup" element={<Signuppage />} />
          <Route
            path="/register/verify/:userToken"
            element={<Emailconfirmation />}
          />
          <Route path="/login" element={<Loginpage />} />
          <Route path="/forgotpassword" element={<Forgotpasswordpage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
