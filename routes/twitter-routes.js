const router = require('express').Router();
const Twitter = require('twitter');
const auth = require('../config/auth.js');
const bodyParser = require('body-parser');

var child_process = require('child_process');

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

      //var outputBuffer = child_process.execSync('python -W ignore ./sentinet.py ' + tweet);

      var sentimentAnalysis = child_process.exec('python -W ignore ./sentinet.py ' + tweet, (error, stdout, stderr) => {
        var output = stdout.toString().trim();
        var resOutputs = output.split('\r');
        for (var i = 0; i < resOutputs.length; i++) {
          resOutputs[i] = resOutputs[i].replace("\n", "");
        }
        console.log("Image URL: " + resOutputs[1])
        console.log("Song URL: " + resOutputs[2])

        res.json({user: req.user, sentiment: resOutputs[0], imageUrl: resOutputs[1], trackUrl:  resOutputs[2]});
      });

    }
    else {
      console.log(error);
      res.status(500).end();
    }
  });
});

module.exports = router;
