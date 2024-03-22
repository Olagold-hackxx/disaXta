import Postcomponent from './Postcomponent'


const Community = () => {
  return (
    <div className='text-2xl   pt-1 md:pt-5 '>
        <h2 className=' text-left ml-5 font-semibold '>Community</h2>
      <div className='border-b-2 pb-1 md:pb-3 text-lg md:text-xl font-semibold'/>
        <Postcomponent category='community' />
    </div>
  )
}

export default Community