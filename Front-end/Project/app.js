var port = 8000;
var express = require(__dirname + '/config/express');
var app = express();
app.listen(port);
module.exports = app;
console.log('Server running on http://localhost:' + port);

/*// Retrieve
var MongoClient = require('mongodb').MongoClient;

// Connect to the db
MongoClient.connect("mongodb://localhost:27017/testdb", function(err, db) {
  if(!err) {
    console.log("Connected to http://localhost:" + port);
  }
});*/