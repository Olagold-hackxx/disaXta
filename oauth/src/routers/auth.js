const express = require("express");
const { oauthSignIn, linkedInOauth, getUserData } = require("../controllers/auth");
const google = require("../config/google");
const linkedin = require("../config/linkedin");
const facebook = require("../config/facebook");
const github = require("../config/github");
const authRouter = express.Router();


//Login user with google
authRouter.get(
  "/google",
  google.authenticate("google", {
    scope: ["profile", "email"],
    failureRedirect: "/error",
    failureFlash: true,
  })
);

//Login user with google
authRouter.get(
  "/new-google",
  google.authenticate("google", {
    scope: ["profile", "email"],
    failureRedirect: "/error",
    failureFlash: true,
    accessType: "offline",
    prompt: "consent",
  })
);
authRouter.get(
  "/google/callback",
  google.authenticate("google", {
    failureRedirect: "/error",
    failureFlash: true,
    session: false,
  }),
  oauthSignIn
);

// Login with facebook
authRouter.get(
  "/facebook",
  facebook.authenticate("facebook", { scope: ["email"] })
);

authRouter.get(
  "/facebook/callback",
  facebook.authenticate("facebook", {
    failureRedirect: "/error",
    failureFlash: true,
  }),
  oauthSignIn
);

// Login with LinkedIn
authRouter.get(
  "/linkedin",
  linkedin.authenticate("linkedin", { scope: ["email", "profile", "openid"] })
);

authRouter.get("/linkedin/callback", linkedInOauth, oauthSignIn);

// Login with github
authRouter.get(
  "/github",
  github.authenticate("github", { failureFlash: true })
);

authRouter.get(
  "/github/callback",
  github.authenticate("github", {
    failureFlash: true,
    failureRedirect: "/error",
  }),
  oauthSignIn
);

authRouter.get(
	"/user",
	getUserData
);

module.exports = authRouter;
