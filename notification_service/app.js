import http from "http"
import config from "./config/config.js"
import { useQueue } from "./lib/queue.js"
import channels from "./constants/channels.js"
import controller from "./services/controller.js"

useQueue(channels.custom_mail, controller.sendCustom)
useQueue(channels.disaster_alert, controller.sendDisasterAlert)
useQueue(channels.forget_password, controller.sendForgetPassword)
useQueue(channels.onboarding, ()=>{})
useQueue(channels.verification, controller.sendVerification)

const server = http.createServer((req, res)=>{
  
})
server.listen(config.server.port, ()=>{
  console.log(`server running on port ${ server.address().port }`)
})