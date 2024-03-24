import { useForm } from "react-hook-form";
import { toast } from "react-toastify";
import axios from "axios";
import Cookies from "js-cookie";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const {
    register,
    handleSubmit,
    //formState: { errors, isSubmitting },
    reset,
  } = useForm();
  const navigate = useNavigate();

  const backendUrl = import.meta.env.VITE_APP_BACKEND_URL;
  const onSubmit = (data) => {
    try {
      const pendingToastId = toast.info("Logging In...", { autoClose: false });
      const loginFn = async () => {
        await axios
          .post(`${backendUrl}/api/user/login/`, data, {
            withCredentials: true,
          })
          .then((response) => {
            console.log(response)
            // Use the cookies as needed
            Cookies.set("token", response.data.token);
            Cookies.set("user", JSON.stringify(response.data.user));
            toast.dismiss(pendingToastId);
            toast.success("Login successful");
            // Reset the form
            reset();

            navigate("/");
          })
          .catch((error) => {
            console.log(error);
            toast.dismiss(pendingToastId);
            toast.error(
              "Login failed. Please make sure the password is correct."
            );
          });
      };
      loginFn();
    } catch (error) {
      // Handle errors (display error toast, etc.)
      console.error("Login error:", error);
      toast.error("Login failed. Please make sure the password is correct.");
    }
  };

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      className="max-w-md mx-auto w-[100%] p-3 bg-gradient-to-r from-fuchsia-500 to-purple-600 md:p-6   rounded-md shadow-md flex flex-col "
    >
      <input
        type="text"
        placeholder="Username"
        className="w-full p-2 mb-4 bg-gradient-to-r from-slate-500 to-slate-800 border rounded focus:border-green focus:outline-none"
        {...register("username")}
      />
      <input
        type="password"
        placeholder="Password"
        className="w-full p-2 mb-4 bg-gradient-to-r  from-slate-500 to-slate-800 border rounded focus:border-green focus:outline-none"
        {...register("password")}
      />
      <input
        className="w-full p-2  bg-gradient-to-r from-fuchsia-500 bg-blue-500 hover:bg-gradient-to-r hover:from-fuchsia-600 hover:to-purple-700 text-white rounded cursor-pointer"
        type="submit"
      />
    </form>
  );
}
