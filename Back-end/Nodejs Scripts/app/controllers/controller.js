module.exports = function(app) {
	
	app.set('json spaces', 2);
	app.get('/', function(request, response) {
		var city = request.query.city.toUpperCase(),
			   state = request.query.state.toUpperCase();
		if ((city != '') && (state != '')) {
			var query = {'Address.State': state, 'Address.City': city};
			var doc = app.locals.db.collection('testcollection3').findOne(query, function(err, doc) {
				if (err) {
					throw err;
					response.send(err);
				} else {
					response.send(doc);
				}
			});
		};
	});
	
};