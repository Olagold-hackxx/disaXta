// import { useForm } from "react-hook-form"; 


export default function Createpost() {
//   const { register, handleSubmit, reset } = useForm();

  //const formError = formState.errors;


  return (
    <form
    //   onSubmit={handleSubmit(onSubmit)}
      className=" p-3 md:p-6 bg-white rounded-md shadow-md flex flex-col"
    >
      <select
        className="w-full p-2 mb-3 border rounded focus:border-green focus:outline-none"
        // {...register("category", { required: true })}
      >
        <option value="">Select Category</option>
        <option value="Community">Community</option>
        <option value="Education">Educational</option>
        <option value="Happening">Happening now</option>
        {/* Add more options as needed */}
      </select>
      <textarea
        type="text"
        placeholder="Description"
        className="w-full p-2 mb-3 border rounded focus:border-green focus:outline-none"
        // {...register("text", { required: true })}
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
