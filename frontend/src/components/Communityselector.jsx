import { NavLink } from "react-router-dom";

const Communityselector = () => {
  return (
    <div className="flex flex-col gap-2 bg-gradient-to-r from-fuchsia-500 to-purple-600 text-black list-none  m-4 rounded-2xl ">
      <NavLink
        className={({ isActive }) =>
          isActive
            ? "hover:bg-graydark p-4 bg-gradient-to-r from-stone-500  to-stone-700  rounded-b-none rounded-2xl"
            : "hover:bg-graydark p-4"
        }
        to={"/"}
      >
        Home
      </NavLink>

      <NavLink
        className={({ isActive }) =>
          isActive
            ? "hover:bg-graydark p-4 bg-neutral-300 bg-gradient-to-r from-stone-500  to-stone-700  "
            : "hover:bg-graydark p-4"
        }
        to={"/community"}
      >
        Community
      </NavLink>
      <NavLink
        className={({ isActive }) =>
          isActive
            ? "hover:bg-graydark p-4 bg-neutral-300 bg-gradient-to-r from-stone-500  to-stone-700   "
            : "hover:bg-graydark p-4"
        }
        to={"/education"}
      >
        Education
      </NavLink>
      <NavLink
        className={({ isActive }) =>
          isActive
            ? "hover:bg-graydark p-4 bg-neutral-300 bg-gradient-to-r from-stone-500  to-stone-700   "
            : "hover:bg-graydark p-4"
        }
        to={"/happeningnow"}
      >
        Happening now
      </NavLink>
      <NavLink
        className={({ isActive }) =>
          isActive
            ? "hover:bg-graydark p-4 bg-neutral-300 bg-gradient-to-r from-stone-500  to-stone-700 rounded-t-none  rounded-2xl "
            : "hover:bg-graydark p-4"
        }
        to={"/disaX-tweet"}
      >
        DisaX
      </NavLink>
    </div>
  );
};

export default Communityselector;
