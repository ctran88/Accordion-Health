var express = require('express');

module.exports = function() {
	var app = express();
	
	app.set('views', __dirname + '/../app/views');
	app.set('view engine', 'jade');
	
	require(__dirname + '/../app/routes/routes')(app);
	
	app.use(express.static(__dirname + '/../public'));
	
	return app;
};