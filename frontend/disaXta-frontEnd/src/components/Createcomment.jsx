// import { useForm } from "react-hook-form";


export default function Createcomment() {
//   const { register, handleSubmit, reset } = useForm();

 
  return (
    <form
    //   onSubmit={handleSubmit(onSubmit)}
      className=" p-3 md:p-6 bg-white rounded-md shadow-md flex flex-col"
    >

      <textarea
        type="text"
        placeholder="Comment"
        className="w-full p-2 mb-3 border rounded focus:border-green focus:outline-none"
        // {...register("comment", { required: true })}
      />
      <input
        type="file"
        className="w-full p-2 mb-3 border rounded focus:border-green focus:outline-none"
        // {...register("picture", { required: false })}
      />
      <button
        className="w-full p-2 bg-green text-white rounded cursor-pointer z-10"
        type="submit"
      >
        Submit
      </button>
    </form>
  );
}


/*Createcomment.propTypes = {
	postId: PropTypes.string,
  };*/