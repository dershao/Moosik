const router = require('express').Router();


//don't want to go to url /profile to get an error - "no such thing as req.user.username"
//check if an user is logged in
const authCheck = (req, res, next) => {
  if (!req.user) {
    //user is not logged in
    res.redirect('/auth/login');
  }
  else {
    //if user is logged in
    //goes to next - see below
    next();
  }
}

router.get("/", authCheck, (req, res) => {
  res.send('Welcome ' + req.user.username);
});

module.exports = router;
