var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var ejs = require('ejs');

app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/public'));

app.get('/', function(req, res){
  res.render('home');
});

app.get('/about', function(req, res){
  res.render('about');
});

app.get('/map/:time/:mode', function(req, res){
  obj = {
        // geocoordinates
        mode: req.params.mode,
        location: "1100 2ND AVENUE #500, SEATTLE, WA 98101",
        time: req.params.time
    }
  res.render('map', obj);
});

app.listen(process.env.PORT || 3000, function(){
    console.log('DEATH RACE 3000!');
});
