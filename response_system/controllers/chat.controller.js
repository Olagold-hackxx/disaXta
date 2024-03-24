const validator = require("../services/validator.service") 

const catchAsyncErrors = require("../lib/catchAsync")

const chatService = require('../services/chat.service')

const postMessage = catchAsyncErrors(async(req, res)=>{
    const validationRes = validator.validateGetByIdObj(req.params)
    if(validationRes.error)return res.status(400).json({message: validationRes.error.message})
    const responseObj = await chatService.generateResponse()
    return res.status(201).json(responseObj)
})

const getMessages = catchAsyncErrors(async(req, res)=>{
    const validationRes = validator.validateGetByIdObj(req.params)
    if(validationRes.error)return res.status(400).json({message: validationRes.error.message})
    const messages = await chatService.getMessages(req.params.id)
    return res.status(200).json(messages)
})

module.exports ={ postMessage, getMessages}