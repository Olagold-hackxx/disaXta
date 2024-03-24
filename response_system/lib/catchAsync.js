function catchAsyncErrors(fn){

    return async(req, res, next)=>{
        try {
            await fn(req, res, next)
        } catch (error) {
            console.log(`error occured: ${error}`)
            return res.status(500).json("internal server error.")
        }
    }

}

module.exports = catchAsyncErrors