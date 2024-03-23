export default function Login() {
  
  return (
    <form
    //   onSubmit={handleSubmit(onSubmit)}
      className="max-w-md mx-auto w-[100%] p-3 bg-gradient-to-r from-fuchsia-500 to-purple-600 md:p-6   rounded-md shadow-md flex flex-col "
    >
      <input
        type="text"
        placeholder="Username, email or phone"
        className="w-full p-2 mb-4 bg-gradient-to-r from-slate-500 to-slate-800 border rounded focus:border-green focus:outline-none"
        // {...register("username")}
      />
      <input
        type="password"
        placeholder="Password*"
        className="w-full p-2 mb-4 bg-gradient-to-r  from-slate-500 to-slate-800 border rounded focus:border-green focus:outline-none"
        // {...register("password")}
      />
      <input
        className="w-full p-2  bg-gradient-to-r from-fuchsia-500 to-purple-600 hover:bg-gradient-to-r hover:from-fuchsia-600 hover:to-purple-700 text-white rounded cursor-pointer"
        type="submit"
      />
    </form>
  );
}
