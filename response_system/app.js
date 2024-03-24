const express = require('express');
require("dotenv").config();
const morgan = require('morgan');
const helmet = require('helmet');
const logger = require('./logger');
const cors = require('cors');
const path = require('path');
const { useQueue } = require('./lib/amqp');
const queues = require('./constants/queues');
const app = express();
const port = process.env.PORT || 3004;
const postsRouter = require("./routes/post.router");
const chatsRouter = require("./routes/chat.router")
const analyzePost = require('./helpers/analyze_post');
const useCron = require('./lib/cron');


// Use middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(helmet());
app.use(morgan('combined'));
app.use(cors());
app.use(express.static(path.join(__dirname, 'views')));

app.use("/api/v1/posts", postsRouter)
app.use("/api/v1/chats", chatsRouter)

useCron()

useQueue(queues.analyze_post, analyzePost)

app.listen(port, () => {
  logger.info(`Server is running on port ${port}`);
});
