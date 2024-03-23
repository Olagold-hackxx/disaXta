import Menu from "./Menu";

const Leftsidebar = () => {
  return (
    <div className=" border-r-2 border-graylight hidden md:block pt-5 ">
      {/* Logo */}
      <div className=" flex gap-3 items-center justify-self-center md:justify-self-start ">
        <div className="w-[70px]">
          <img src="../../Vector.png" />
        </div>
        <div className="flex flex-col  font-semibold text-[24px]">
          <h1>Climate</h1>
          <h1>Wavers</h1>
        </div>
      </div>
      <Menu />
      {/* Name box */}
      <div className="flex flex-row items-center my-6 self-center ">
        {/* Img here */}
        <img src="../../pic1.png" className="mr-2" />
        <div>
          <h3>Titi Simon</h3>
          <p>@titisimon21</p>
        </div>
      </div>
    </div>
  );
};

export default Leftsidebar;
