import amqp from "amqplib"
import config from "../config/config.js"

export async function useQueue(channel_name, func){
    try{
    const conn = await amqp.connect(config.amqp.url)
    const channel = await conn.createChannel()
    channel.assertQueue(channel_name, {durable: false})
    .then(res=>{ console.log(`info: channel ${channel_name} asserted.`)})
    channel.consume(channel_name, async(msg)=>{
        if(msg !== null){
            const parsed = JSON.parse(msg.content)
            try{
                await func(parsed)
            }catch(ex){
                console.log(`useQueue callback function failed - ${ex}`)
            }
            channel.ack(msg)
        }
    })
    }catch(err){
        console.log("amqp error: ", err)
    }
}