const express = require('express');
const cookieSession = require('cookie-session');
const passport = require('passport');
const authRoutes = require('./routes/auth-routes.js');
const profileRoutes = require('./routes/profile-routes.js');
const bodyParser = require('body-parser');
const dbURL = require('./config/database.js');
const mongoose = require('mongoose');
const passportSetup = require('./config/passport.js');
const auth = require('./config/auth.js');
const twitterRoutes = require('./routes/twitter-routes.js');
const appRoutes = require('./routes/app-routes.js');

const PORT = process.env.PORT || 3000;

var app = express();

app.set('view engine', 'ejs');

app.use(cookieSession({
  maxAge: 24 * 60 * 60 * 1000,
  keys: ["anything"]
}));

//initialize passport
app.use(passport.initialize());
//initialize session cookies for passport
app.use(passport.session());

//serve static files
app.use(express.static("./public"));

//store users in database
mongoose.connect(dbURL.url, () => {
  console.log("Connected to database!");
});

//set up routers
app.use('/auth', authRoutes);
app.use('/twitter', twitterRoutes);
app.use('/app', appRoutes);

app.get('/', (req, res) => {
  res.render('index');
});

app.listen(PORT);
console.log("Listening to port %s...", PORT);
