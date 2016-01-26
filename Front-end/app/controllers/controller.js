module.exports = function(app) {
	// route to view full mongodb dataset
	app.get('/', function(req, res) {
		var docArray = [];
			
		app.locals.db.collection('NPPES_collection').find({}, {_id: 0, Specialization: 1, 'Address.City': 1, 'Address.State': 1, 'Address.Zip Code': 1, 'Address.Latitude': 1, 'Address.Longitude': 1}).toArray(function(err, result) {
			if (err) throw err;
			
			for (var i = 0; i < result.length; i++) {
				docArray.push(result[i]);
			}
			
			return res.render('index', {jsonData: docArray});
		});
	});

	// route to pull mongodb data via query parameters
	app.get('/search', function(req, res) {
		var query = {};
		var docArray = [];

		// city query
		if (req.query.city && req.query.state) {
			query = {'Address.City': req.query.city.toUpperCase(), 'Address.State': req.query.state.toUpperCase()};
			
			app.locals.db.collection('NPPES_collection').find(query, {_id: 0, Specialization: 1, 'Address.City': 1, 'Address.State': 1, 'Address.Zip Code': 1, 'Address.Latitude': 1, 'Address.Longitude': 1}).toArray(function(err, result) {
				if (err) throw err;
				
				for (var i = 0; i < result.length; i++) {
					docArray.push(result[i]);
				}
				
				return res.render('index', {jsonData: docArray});
			});
		}

		// state query
		else if (req.query.state) {
			query = {'Address.State': req.query.state.toUpperCase()};
			
			app.locals.db.collection('NPPES_collection').find(query, {_id: 0, Specialization: 1, 'Address.City': 1, 'Address.State': 1, 'Address.Zip Code': 1, 'Address.Latitude': 1, 'Address.Longitude': 1}).toArray(function(err, result) {
				if (err) throw err;
				
				for (var i = 0; i < result.length; i++) {
					docArray.push(result[i]);
				}
				
				return res.render('index', {jsonData: docArray});
			});
		}

		// zip code query
		else if (req.query.zip) {
			query = {'Address.Zip Code': req.query.zip};
			
			app.locals.db.collection('NPPES_collection').find(query, {_id: 0, Specialization: 1, 'Address.City': 1, 'Address.State': 1, 'Address.Zip Code': 1, 'Address.Latitude': 1, 'Address.Longitude': 1}).toArray(function(err, result) {
				if (err) throw err;
				
				for (var i = 0; i < result.length; i++) {
					docArray.push(result[i]);
				}
				
				return res.render('index', {jsonData: docArray});
			});
		}

		// no query found; returns empty map
		else {
			res.render('index', {jsonData: docArray});
		}
	});
};