var express = require('express');

module.exports = function() {
	var app = express();
	require(__dirname + '/../app/routes/routes')(app);
	return app;
};