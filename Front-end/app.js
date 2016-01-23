// environment
process.env.NODE_ENV = process.env.NODE_ENV || 'development';

// modules
var MongoClient = require('mongodb').MongoClient,
	   config = require(__dirname + '/config/config'),
	   express = require(__dirname + '/config/express'),
	   app = express();

// connect to mongoDB
MongoClient.connect(config.db, function(err, db) {
	if (err) {
		throw err;
		console.dir(err);
	}
	app.locals.db = db;
	console.log('Connected to MongoDB successfully.');
});

// start application
app.listen(config.port);
console.log(process.env.NODE_ENV + ' server running at http://localhost:' + config.port);