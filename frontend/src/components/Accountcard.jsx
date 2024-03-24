import { useState } from "react";
import PropTypes from "prop-types";

const Accountcard = ({ user }) => {
  const [isFollow, setIsFollow] = useState(false);
  //const [followStyle, setFollowStyle] = useState('bg-black text-xs text-white font-semibold py-2 px-3 ml-2 rounded-xl')

  //const unfollowStyles = ' after:content-[Unfollow] after:bg-white-100 after:outline after:outline-3 after:outline-black-500 after:text-white-500 '

  return (
    <div className="flex flex-row items-center px-3 py-1 justify-between ">
      <div className="flex flex-row items-center self-center ">
      <img
            src={user.profile_pic ? user.profile_pic : "../../avatar.png"}
            className="mr-2 rounded-full h-12"
            alt="Profile Pic"
          />{" "}
        <div>
          <h3>{user.first_name}</h3>
          <p>@{user.username}</p>
        </div>
      </div>
      <button
        // style={followStyle}
        className={`bg-black text-xs text-white font-semibold py-2 px-3 ml-2  rounded-xl ${
          isFollow &&
          "bg-stone-100 outline outline-3 outline-stone-900 !text-slate-700 before:hover:content-['']  hover:bg-green-100 hover:outline hover:outline-3 hover:outline-black-500 hover:text-black-500 "
        } `}
      >
        {isFollow === true ? "Following" : "Follow"}
      </button>
    </div>
  );
};

Accountcard.propTypes = {
  user: PropTypes.object,
};

export default Accountcard;
