const { Router } = require("express")
const { postMessage, getMessages } = require("../controllers/chat.controller")

const router = Router()

router.post("/:id", postMessage)
router.get('/:id', getMessages)


module.exports = router