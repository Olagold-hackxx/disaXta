const dotenv = require("dotenv")

dotenv.config()

const openai = {
    apiKey: process.env.OPENAI_API_KEY
}

const amqp = {
    url: process.env.AMQP_URL
}

// const firebase = {
//     "type": process.env.FIREBASE_TYPE,
//     "project_id": process.env.FIREBASE_PROJECT_ID,
//     "private_key_id": process.env.FIREBASE_PRIVATE_KEY_ID,
//     "private_key": process.env.FIREBASE_PRIVATE_KEY,
//     "client_email": process.env.FIREBASE_CLIENT_EMAIL,
//     "client_id": process.env.FIREBASE_CLIENT_ID,
//     "auth_uri": process.env.FIREBASE_AUTH_URI,
//     "token_uri": process.env.FIREBASE_TOKEN_URI,
//     "auth_provider_x509_cert_url": process.env.FIREBASE_AUTH_PROVIDER_CERT_URL,
//     "client_x509_cert_url": process.env.FIREBASE_CLIENT_CERT_URL,
//     "universe_domain": process.env.FIREBASE_UNIVERSE_DOMAIN,
//     projectId: process.env.FIREBASE_PROJECT_ID,
//   }

const firebaseConfig = {
    apiKey: "AIzaSyBLE5GPSjQBS-xVQwmoqcHen3nwo8pinv4",
    authDomain: "disaxta.firebaseapp.com",
    projectId: "disaxta",
    storageBucket: "disaxta.appspot.com",
    messagingSenderId: "196170474315",
    appId: "1:196170474315:web:c35b4fc71582023e7e3ece",
    measurementId: "G-89W69YVLGQ"
  }

  const gemini = {
    apiKey: process.env.GEMINI_API_KEY
  }

  const aiModels = {
    prediction: process.env.PREDICTION_AI_MODEL,
    recognition: process.env.RECOGNITION_AI_MODEL
  }

module.exports = {
    openai,
    firebase: firebaseConfig,
    amqp,
    gemini,
    aiModels
}