module.exports = function(app) {
	
	app.set('json spaces', 2);
	app.get('/', function(request, response) {
		var city = request.query.city.toUpperCase(),
			   state = request.query.state.toUpperCase();
		var query = {'Address.State': state, 'Address.City': city};
		
		if ((city != '') && (state != '')) {
			var doc = app.locals.db.collection('testcollection').findOne(query, function(err, doc) {
				if (err) {
					throw err;
					response.send(err);
				} else {
					response.send(doc);
				}
			});
		}
	});
	
};