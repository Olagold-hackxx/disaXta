
export default function Signupform() {
  // const { register, handleSubmit, reset, formState } = useForm();

  return (
    <form
      // onSubmit={handleSubmit(onSubmit)}
      className="max-w-md mx-auto text-black p-3 md:p-6 bg-white rounded-md shadow-md flex flex-col"
    >
      {/* Your input fields go here with register calls */}
      <div className="flex flex-row gap-2 ">
        <input
          type="text"
          className="w-full p-2 mb-3 border rounded focus:border-green focus:outline-none"
          placeholder="First name*"
          // {...register("first_name", { required: true, maxLength: 80 })}
        />

        <input
          type="text"
          placeholder="Last name*"
          className="w-full p-2 mb-3 border rounded focus:border-green focus:outline-none"
          // {...register("last_name", { required: true, maxLength: 100 })}
        />
      </div>
      <input
        type="text"
        placeholder="Username*"
        className="w-full p-2 mb-3 border rounded focus:border-green focus:outline-none"
        // {...register("username", { required: true, maxLength: 100 })}
      />{" "}
      <input
        type="text"
        placeholder="Bio"
        className="w-full p-2 mb-3 border rounded focus:border-green focus:outline-none"
        // {...register("bio", { required: false })}
      />
      <input
        type="password"
        placeholder="Password*"
        className="w-full p-2 mb-3 border rounded focus:border-green focus:outline-none"
        // {...register("password", { required: true, maxLength: 20 })}
      />
      {/* {formError.password && formError.password.type === "maxLength" && (
        <span className="text-red-500 text-sm mb-4 ">
          Password length is too long
        </span>
      )} */}
      <input
        type="text"
        placeholder="Email"
        className="w-full p-2 mb-3 border rounded focus:border-green focus:outline-none"
        // {...register("email", { required: true, pattern: /^\S+@\S+$/i })}
      />
      {/* {formError.email && formError.email.type === "pattern" && (
        <span className="text-red-500 text-sm mb-4 ">
          This is not a valid email!
        </span>
      )} */}
      <input
        type="tel"
        placeholder="Mobile number"
        className="w-full p-2 mb-3 border rounded focus:border-green focus:outline-none"
        // {...register("mobileNumber", {
        //   required: true,
        //   minLength: 6,
        //   maxLength: 12,
        //   pattern: /^\d+$/,
        // })}
      />
      {/* {formError.mobileNumber &&
        formError.mobileNumber.type === "maxLength" && (
          <span className="text-red-500 text-sm mb-4 ">
            Phone number is too long{" "}
          </span>
        )}
      {formError.mobileNumber &&
        formError.mobileNumber.type === "minLength" && (
          <span className="text-red-500 text-sm mb-4 ">
            Phone number is too short{" "}
          </span>
        )}
      {formError.mobileNumber && formError.mobileNumber.type === "pattern" && (
        <span className="text-red-500 text-sm mb-4 ">
          Please make sure this is a valid phone number{" "}
        </span>
      )} */}
      <button
        className="w-full p-2 bg-green text-white rounded cursor-pointer z-10"
        type="submit"
      >
        Submit
      </button>
    </form>
  );
}
