const router = require('express').Router();
const passport = require('passport');

// auth login
router.get('/login', (req, res) => {
  res.render('login', { user: req.user});
});

router.get('/logout', (req, res) => {
  req.session.destroy();
  res.redirect('/');
});

//auth with twitter
router.get('/twitter', passport.authenticate('twitter'));


router.get('/twitter/callback', passport.authenticate('twitter'), (req, res) => {

  res.render('app', {user: req.user, sentiment: null, imageUrl: null, trackUrl: null});
});

module.exports = router;
