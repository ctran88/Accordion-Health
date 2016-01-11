var MongoClient = require('mongodb').MongoClient,
	   config = require(__dirname + '/../../config/config'),
	   assert = require('assert');
	   
module.exports = function(app) {
	/*
	app.set('json spaces', 2);
	app.get('/', function(request, response) {
		var city = request.query.city;
		var state = request.query.state;
		
		if ((city == 'austin') && (state == 'texas')) {
			response.json({
				city: city,
				state: state,
				latitude: '30.2837',
				longitude: '-97.7326'
			});
		} else if ((city == '') || (state == '')) {
			response.send('You must input both a city and state for coordinates.');
		} else if ((city != 'austin') || (state != 'texas')) {
			response.send('Sorry, we do not have the coordinates for ' + city + ', ' + state);
		}
	});*/
	
	// connect to mongoDB
		var cursor = db.collection('testcollection3').find({State:"TX"});
		cursor.each(function(err, doc) {
			assert.equal(err, null);
			if(doc != null) {
				console.log('document found');
				console.dir(doc);
			} else {
				console.log('no document exists');
				callback();
			}
		});

};