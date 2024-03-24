import Menu from "./Menu";
import PropTypes from "prop-types";

const Leftsidebar = ({ user }) => {
  return (
    <div className=" border-r-[1px] border-gray-500 hidden md:block pt-5 ">
      {/* Logo */}
      <div className=" flex gap-3 items-center justify-self-center md:justify-self-start ">
        <div className="w-[70px]">
          <img src="../../Vector.png" />
        </div>
        <div className="flex flex-col  font-semibold text-[24px]">
          <h1>DisaXta</h1>
        </div>
      </div>
      <Menu />
      {/* Name box */}
      <div className="flex flex-row items-center my-6 self-center ">
        {/* Img here */}
        <img
          src={"../../avatar.png"}
          className="mr-2 rounded-full h-12"
          alt="Profile Pic"
        />

        <div>
          <h3>{"first_name"}</h3>
          <p>@{"username"}</p>
        </div>
      </div>
    </div>
  );
};

Leftsidebar.propTypes = {
  user: PropTypes.object,
};

export default Leftsidebar;
