const axios = require("axios")
const config = require("../config/config")

async function getPredictions(p){
    const prediction = await axios.post(config.aiModels.prediction, p)
    return prediction.data
}

module.exports = { getPredictions}