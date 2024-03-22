// import { useForm } from 'react-hook-form';
import {BiArrowBack} from "react-icons/bi"
import { Link } from 'react-router-dom';


const Forgotpassword = () => {

   /*  const {
        register,
        handleSubmit,
        watch,
        formState: { errors },
      } = useForm();
      const onSubmit = (data) => {

        console.log(data)
        reset()
      }; */

  return (
    <div>
        <Link to={'/login'} ><BiArrowBack size={32} className='absolute -top-[180px] left-4 hover:cursor-pointer  ' /></Link>
        <p className='mb-4'>Enter your email, phone, or and we'll send you a link to get back into your account.</p>
        <form className='flex flex-col gap-3 mx-10 ' >
            <input
            type="text"
            placeholder="Username, email or phone"
            className="w-full text-black p-2 mb-4 border rounded focus:border-green focus:outline-none"
            // {...register("username", {required: true, maxLength: 100})}
             />
            <input
            className="w-full p-5 text-xl font-medium
             bg-gradient-to-r from-fuchsia-500 to-purple-600 hover:bg-gradient-to-r hover:from-fuchsia-600 hover:to-purple-700 text-white rounded cursor-pointer"
            type="submit" />
        </form>
    </div>
  )
}

export default Forgotpassword