import { useState } from 'react'
import {HiOutlineMenuAlt1} from "react-icons/hi"
import {AiOutlineSearch} from "react-icons/ai"
import Mobilemenu from './Mobilemenu'

const Topbar = () => {

  const [isOpen, setIsOpen] = useState(false)


  return (
    // <Padder >  flex flex-row
    <div className=' grid grid-cols-[1fr_2fr_1fr] items-center outline outline-1 outline-graylight px-3 py-2 md:px-20 md:py-4 '>
        {/* Page title */}
        <HiOutlineMenuAlt1 size={35} onClick={() => setIsOpen(true)} />
        {
          isOpen === true ?
            <Mobilemenu setIsOpen={setIsOpen} />
          :
            null
        }
        {/* Logo */}
        <div className=' justify-self-center md:justify-self-start '>
            <img src='../../Logo.png'/>
        </div>
        {/* Search btn */}
        {/* <div className='  w-[60%] justify-self-end '> */}
          <AiOutlineSearch  size={35} className='justify-self-end' />
        {/* </div> */}
    </div>
    // </Padder>
  )
}

export default Topbar