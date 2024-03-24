import React from "react";
import Accountcard from "./Accountcard";

const Popularaccounts = () => {
  const user = {
    "first_name": "Cartesi",
    "last_name": "Rollups",
    "profile_pic": "../../avatar.png",
    "username": "cartesi"

  }
  
  return (
    <div>
      <div className="flex flex-col gap-2 text-black bg-gradient-to-r from-fuchsia-500 to-purple-600 list-none py-4 m-4 rounded-2xl ">
        <h2 className="text-lg font-semibold p-3">Popular accounts</h2>
        <Accountcard user={user} />
        <Accountcard user={user} />
        <Accountcard user={user} />
      </div>
    </div>
  );
};

export default Popularaccounts;
