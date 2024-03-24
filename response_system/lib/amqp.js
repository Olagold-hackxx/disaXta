const amqp = require("amqplib")
const config = require("../config/config")

const useQueue = async function(queueName, callback){
    try{
        const conn = await amqp.connect(config.amqp.url)
        const channel = await conn.createChannel()
        channel.assertQueue(queueName, {durable: false})
        .then(res=>{ console.log(`info: channel ${queueName} asserted.`)})
        channel.consume(queueName, async(msg)=>{
            if(msg !== null){
                const parsed = JSON.parse(msg.content)
                try{
                    await callback(parsed)
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

const sendToQueue = async function(queueName, data){
    const conn = await amqp.connect(config.amqp.url)
        const channel = await conn.createChannel()
        channel.assertQueue(queueName, {durable: false})
        const str = JSON.stringify(data)
        channel.sendToQueue(queueName, Buffer.from(str))
}

module.exports = { useQueue, sendToQueue }