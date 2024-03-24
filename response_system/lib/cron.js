const cron = require("node-cron")
const postService = require("../services/post.service")
const aiService = require("../services/ai.service")
const aiConfig = require("../config/ai")

function useCron(){
    cron.schedule("* * 6 * *", async function(){
        console.log("cron job started")
        const body = await aiService.generateEducativeQuote()
        const post = await postService.create({userId: aiConfig.id, username: aiConfig.username, body})
    })
}

module.exports = useCron