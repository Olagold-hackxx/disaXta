import Postcomponent from './Postcomponent'


const Happeningnow = () => {
  return (
    <div className='text-2xl text-center border-b-2   pt-1 md:pt-5 '>
        <h2 className='pb-1 md:pb-3 text-lg  border-b-2  p-6  md:text-xl font-semibold '>Happening Now</h2>
        <Postcomponent  category="happening"/>
    </div>
  )
}

export default Happeningnow