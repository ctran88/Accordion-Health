// environment
process.env.NODE_ENV = process.env.NODE_ENV || 'development';

// modules
var MongoClient = require('mongodb').MongoClient,
	   config = require(__dirname + '/config/config'),
	   express = require(__dirname + '/config/express'),
	   app = express();

// start application
app.listen(config.port);
console.log(process.env.NODE_ENV + ' server running at http://localhost:' + config.port);

// connect to mongoDB
MongoClient.connect(config.db, function(err, db) {
	module.exports = app;
});