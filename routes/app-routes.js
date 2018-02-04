const router = require('express').Router();

const authCheck = (req, res, next) => {
  if (!req.user) {
    //user is not logged in
    res.redirect('/');
  }
  else {
    next();
  }
}
router.get('/', authCheck, (req, res) => {
  res.render('app', {user: req.user, sentiment: null, imageUrl: null, trackUrl: null});
});

module.exports = router;
