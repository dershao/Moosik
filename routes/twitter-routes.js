const router = require('express').Router();
const Twitter = require('twitter');
const auth = require('../config/auth.js');
const bodyParser = require('body-parser');

var spawn = require('child_process').spawn;

const TAG = "moosik";

var urlencodedParser = bodyParser.urlencoded({extended: false});

router.post('/', urlencodedParser, (req, res) => {

  var client = new Twitter({
    consumer_key: auth.twitterAuth.consumerKey,
    consumer_secret: auth.twitterAuth.consumerSecret,
    access_token_key: auth.twitterAuth.accessToken,
    access_token_secret: auth.twitterAuth.accessSecret
  });

  var params = {screen_name: req.body.name, count: 4};
  client.get('statuses/user_timeline', params, function(error, tweets, response) {

    var tweet = "";

    if (!error) {
      for (var i = 0; i < tweets.length; i++) {
        if (tweets[i]['entities']['hashtags'][0] && tweets[i]['entities']['hashtags'][0]['text']) {
          tweet = tweets[i]['text'];
          break;
        }
      }
      console.log(tweet);
      var process = spawn("python", ["-W ignore ../sentinet.py " + tweet]);
      process.stdout.on('close', function(chunk) {
        var textChunk = chunk.toString('utf8');
        print(textChunk);
      });
    }
    else {
      console.log(error);
    }
  });
  res.status(200).end();
});


module.exports = router;
