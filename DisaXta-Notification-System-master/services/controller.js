import mailDataValidator from "../validation/mail.js"
import mailer from "./mailer.js"

class Controller{

    async sendDisasterAlert(d){
        const { emails, data} = d
        const validationErr = mailDataValidator.validateDisasterAlertEmailData(data).error
        if(!emails.length || validationErr){
            console.log(validationErr)
            return
        }
        for(let email of emails){
            try{
                await mailer.sendDisasterAlert(email, data)
            }catch(ex){
                console.log(ex)
                continue;
            }

        }

    }

    async sendCustom(d){
        const {  emails, email, data} = d
        if(!emails && !email)return
        const validationErr = mailDataValidator.validateCustomEmailData(data).error
        if(validationErr){
            console.log(validationErr)
            return
        }
        if(email){
            try {
                await mailer.sendCustom(email, data)
            } catch (error) {
                console.log(error)
            }
        }
        if(emails){
            for(let email of emails){
                try{
                    await mailer.sendCustom(email, data)
                }catch(ex){
                    console.log(ex)
                    continue;
                }
    
            }
        }
    }

    sendForgetPassword(d){
        const { email, data } = d
        if(!email)return 
        const validationErr = mailDataValidator.validateForgetPasswordEmailData(data).error
        if(validationErr){
            console.log(validationErr)
            return
        }
        try {
            mailer.sendForgetPassword(email, data)
        } catch (error) {
            console.log(`mail error: ${error}`)
        }

    }

    async sendVerification(d){
        const {email, data} = d
        if(!email)return
        const validationErr = mailDataValidator.validateVerificationEmailData(data).error
        if(validationErr){
            console.log(validationErr)
            return
        }
        
        try {
            await mailer.sendVerification(email, data)
        } catch (error) {
            console.log(`mail error: ${error}`)
        }
    }

    
}

export default Object.freeze(new Controller())