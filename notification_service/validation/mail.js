import Joi from "joi"

class MailValidation{
    validateForgetPasswordEmailData(data){
        return Joi.object({
            url: Joi.string()
        }).validate(data)
    }
    validateDisasterAlertEmailData(data){
        return Joi.object({
            location: Joi.string().required(),
            disasterType: Joi.string().required()
        }).validate(data)
    }
    validateCustomEmailData(data){
        return Joi.object({
            content: Joi.string().required()
        }).validate(data)
    }
    validateVerificationEmailData(data){
        console.log(data)
        return Joi.object({
            code: Joi.string().required()
        }).validate(data)
    }
}

const mailDataValidator =  new MailValidation()

export default Object.freeze(mailDataValidator)