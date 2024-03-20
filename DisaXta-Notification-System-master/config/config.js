import dotenv from "dotenv"
import Joi from "joi"

dotenv.config()

const amqp = {
    url: process.env.AMQP_URL || "amqp://localhost",

}

const server = {
    port: process.env.SERVER_PORT,
    host: process.env.SERVER_HOST,
    protocol: process.env.SERVER_PROTOCOL,
    secret: process.env.SERVER_SECRET
}


const mail = {
    auth: {user: process.env.MAIL_USER,
    pass: process.env.MAIL_PASS,
    },
    host: process.env.MAIL_HOST,
    port: process.env.MAIL_PORT,
    service: process.env.MAIL_SERVICE
}

const config = {
    amqp,
    server,
    mail
}

const validateResult = Joi.object({
    server: Joi.object({
        port: Joi.string(),
        host: Joi.string(),
        protocol: Joi.string(),
        secret: Joi.string()
    }),
    amqp: Joi.object({
        url: Joi.string().required(),
    }),
    mail: Joi.object({
        auth: Joi.object({
            user: Joi.string().required(),
            pass: Joi.string().required()
        }),
        port: Joi.string().required(),
        host: Joi.string().required(),
        service: Joi.string().required()
    })

}).validate(config)

if(validateResult.error){
    throw Error(validateResult.error.message)
}

export default config