import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Accountcard from "./Accountcard";
import { AiFillHeart, AiOutlineRetweet } from "react-icons/ai";
import { HiOutlineChatBubbleOvalLeft } from "react-icons/hi2";
import { PiBookmarkFill } from "react-icons/pi";
import { TbLineDashed } from "react-icons/tb";


const Postcomponent = ({ category = "" }) => {
 const [posts, setPosts] = useState([]);
  const navigate = useNavigate();
  const [isLike, setIsLike] = useState(false);
  const [isSave, setIsSave] = useState(false);


  return (
    <div className=" py-3 border-b-2">
      {posts.map((post, index) => (
        <div key={index} className="border-b border-gray-300 py-4">
          <Accountcard userId={post.user} />
          <div onClick={() => handlePostClick(post)}>
            <p className="text-left text-sm px-3 my-3 ">{post.content_text}</p>
            <img
              className="w-[100%] px-3 "
              src={`${backendUrl}/api/v1/backend${post.content_image}`}
              alt=""
            />
          </div>
          <div className="flex flex-row justify-between px-3 mt-2 ">
            <div
              className="flex flex-row items-center "
              onClick={() => {
                handleLike(post.id, index);
              }}
            >
              <AiFillHeart size={18} color={post.isLike ? "#ff0000" : ""} />
              <p className="text-xs ml-1 ">{post.likers_count}</p>
            </div>
            <div className="flex flex-row items-center  ">
              <AiOutlineRetweet size={18} />
              <p className="text-xs ml-1 ">{post.comment_count}</p>
            </div>
            <div className="flex flex-row items-center  ">
              <HiOutlineChatBubbleOvalLeft size={18} />
              <p className="text-xs ml-1 ">{post.comments_count}</p>
            </div>
            <div
              className="flex flex-row items-center"
              onClick={() => {
                handleSave(post.id, index);
              }}
            >
              <PiBookmarkFill
                size={18}
                color={post.isSave ? "rgb(0 128 128 / 1)" : ""}
              />
              <p className="text-xs ml-1 ">{post.savers_count}</p>
            </div>
            <div className="flex flex-row items-center  ">
              <TbLineDashed size={18} />
              {/* <p className='text-xs ml-1 '>2</p> */}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};


export default Postcomponent;
