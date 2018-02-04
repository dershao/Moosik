const passport = require('passport');
const TwitterStrategy = require('passport-twitter').Strategy;
const configAuth = require('./auth.js');
const User = require('../models/User.js');

passport.serializeUser((user, done) => {
  done(null, user.id);
}),

passport.deserializeUser(function(id, done) {
  User.findById(id, (err, user) => {
    done(err, user);
  });
}),

passport.use(new TwitterStrategy ({

  consumerKey : configAuth.twitterAuth.consumerKey,
  consumerSecret : configAuth.twitterAuth.consumerSecret,
  callbackURL : configAuth.twitterAuth.callbackURL
  
}, (token, tokenSecret, profile, done) => {

  User.findOne({twitterId: profile.id}).then( (currentUser) => {
    if (currentUser) {
      console.log("user is: " + currentUser);
      done(null, currentUser);
    } else {

      new User({
        username: profile.username,
        twitterId: profile.id
      }).save().then((newUser) => {
        console.log("new user was created: " + newUser);
        done(null, newUser);
      });
    }
  });
}));
