
import { useState } from "react";
import { AiOutlineSend } from "react-icons/ai";
import { useParams } from "react-router-dom";

const Chatcomponent = () => {
  const [textValue, setTextValue] = useState("");
  const [isSubmited, setIsSubmited] = useState("");
  const [receivedMessages, setReceivedMessages] = useState([]);
  const [allMessages, setAllMessages] = useState([]);

  return (
    <div className="max-h-fit h-[90%] flex flex-col justify-between">
      <div className="overflow-auto">
        {allMessages.map((message, index) => (
          <div key={index}>{message}</div>
        ))}
        {receivedMessages.map((message, index) => (
          <div key={index}>{message}</div>
        ))}
      </div>
      <div className="bg-graylight p-1 mx-5 md:p-2 border-2 border-graydark  rounded-full flex flex-row items-center ">
        <input
          className="justify-self-end bg-transparent w-[80%] focus:outline-0 focus:bg-gray-200 focus:rounded-full p-2 text-black "
          value={textValue}
          onChange={(e) => setTextValue(e.target.value)}
          type="text"
          placeholder="Ask disaX a question."
        />{" "}
        <AiOutlineSend
          size={25}
          onClick={handleSubmit}
          className="items-end p-.5 ml-3 cursor-pointer "
          type="submit"
        />
      </div>
    </div>
  );
};

export default Chatcomponent;
