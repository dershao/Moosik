const router = require('express').Router();
const passport = require('passport');

// auth login
router.get('/login', (req, res) => {
  res.render('login', { user: req.user});
});

router.get('/logout', (req, res) => {
  req.logout();
  res.redirect('/');
});

//auth with twitter
router.get('/twitter', passport.authenticate('twitter'));


router.get('/twitter/callback', passport.authenticate('twitter'), (req, res) => {

  res.redirect('/app');
});

module.exports = router;
