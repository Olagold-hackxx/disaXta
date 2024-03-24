const { Router } = require("express")
const { createPost, getPosts, getPost, getPostReplies, likePost, getPostsByUserId } = require("../controllers/post.controller")

const router = Router()

router.post("/", createPost)
router.get("/", getPosts)
router.get("/:id/replies", getPostReplies)
router.get("/:id", getPost)
router.get("/by-userId/:id", getPostsByUserId)
router.patch("/:id", likePost)

module.exports = router