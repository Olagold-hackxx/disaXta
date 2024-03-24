const Joi = require("joi")

class Validator{
   validatePost(obj){
    return Joi.object({
        username: Joi.string().required(),
        userId: Joi.string().required(),
        body: Joi.string().required(),
        replyTo: Joi.string(),
        image: Joi.string()
    }).validate(obj)
    } 

    validateAiPayload(obj){
        return Joi.object({
            postId: Joi.string().required(),
            body: Joi.string().required(),
            image: Joi.string()
        }).validate(obj)
    }

    validateGetByIdObj(obj){
        return Joi.object({
            id: Joi.string().required()
        }).validate(obj)
    }
    

}

const validator = new Validator()

module.exports = validator
    