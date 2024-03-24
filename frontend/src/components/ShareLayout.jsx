import Topbar from "./Topbar";
import Leftsidebar from "./Leftsidebar";
import Rightsidebar from "./Rightsidebar";
import { Outlet } from "react-router-dom";
import Cookies from "js-cookie";



const SharedLayout = () => {
  const user = JSON.parse(Cookies.get("user"));
  console.log(user)
  
  return (
    <div className='bg-gradient-to-r from-slate-900 to-slate-700 text-white h-screen'>
      <div className=" block md:hidden ">
        <Topbar />
      </div>
      <div className="grid grid-cols-1 md:grid-cols-[1fr_2fr_1fr] px-2 md:px-10 ">
        <Leftsidebar user={user} />
        {/* <Mainfeed/> */}
        <Outlet />
        <Rightsidebar />
      </div>
    </div>
  );
};

export default SharedLayout;