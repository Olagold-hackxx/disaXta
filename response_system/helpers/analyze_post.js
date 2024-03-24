const aiService = require("../services/ai.service")
const postService = require("../services/post.service")
const { getPredictions } = require("./get_prediction")

async function analyzePost(obj){
    try{
    const {id: postId} = obj
    const post = await postService.getById(postId)
    const catIndex = await aiService.checkChatCategory(post.body)
    console.log({catIndex})
    if(catIndex == "2" || catIndex == "3"){
        const body = `hello @${post.username} thank you for providing this information, we are currently analyzing your post, we will make a post to address the public as soon as possible. We also advice making a report containing location,   on disaXta reports section`
        await postService.create({userId: "12345", username: "X-AI", body, replyTo: post.id})
        return
    }
    if(catIndex == "0"){
        const body = `hello @${post.username} we noticed you flagged this post as a disaster related post, kindly refrain from this action to prevent raising false alarm to the public`
        const r = await postService.create({userId: "12345", username: "X-AI", body, replyTo: post.id})
        console.log({r})
        return
    }
    if(catIndex == "1"){
        try {
            const body = await aiService.handleChatResponse(post.body)
            await postService.create({userId: "12345", username: "X-AI", body, replyTo: post.id})
        return
        } catch (error) {
            
        }
    }
    }catch(err){
        console.log(err)
    }
}

module.exports = analyzePost