var express     = require('express');
var app         = express();
var bodyParser  = require('body-parser');
var ejs         = require('ejs');
var modes       = require('./public/modes.json');

app.set('view engine', 'ejs');

app.use(express.static(__dirname + '/public'));
app.use(bodyParser.urlencoded({extended: false}));

app.get('/', function(req, res){
  res.render('home');
});

app.get('/about', function(req, res){
  res.render('about');
});

app.post('/process', function(req,res){
  res.send({result: true})
});

app.get('/map/:time/:mode/:location', function(req, res){
  var time = req.params.time
  var mode = req.params.mode
  var location = req.params.location
  var match = modes.modes.filter(function(val, index, array) {
      return val.name === mode;
  });
  var icon = (match[0].icon)


  res.render('map', {time: time, mode:mode, location:location, icon:icon, modes:modes.modes});
})

app.listen(process.env.PORT || 3000, function(){
    console.log('DEATH RACE 3000!');
});
