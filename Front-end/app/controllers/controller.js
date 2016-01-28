module.exports = function(app) {
	var query = {};
	var emptyArray = {};

	// function to retrieve data from mongo
	function mongoQuery(res, query) {
		app.locals.db.collection('NPI_collection').find(query, {_id: 0, 'NPI': 0, 'Taxonomy': 0, 'Middle Name': 0}).toArray(function(err, result) {
				var docArray = [];
				if (err) throw err;
				
				for (var i = 0; i < result.length; i++) {
					docArray.push(result[i]);
				}
				
				return res.render('index', {jsonData: docArray});
			});
	}

	// route to display empty map
	app.get('/', function(req, res) {
		res.render('index', {jsonData: emptyArray});
	});

	// route to view full mongodb dataset
	app.get('/viewall', function(req, res) {
		mongoQuery(res, query);
	});

	// route to pull mongodb data via query parameters
	app.get('/search', function(req, res) {
		// city query
		if (req.query.city && req.query.state) {
			query = {'Address.City': req.query.city.toUpperCase(), 'Address.State': req.query.state.toUpperCase()};
		}

		// state query
		else if (req.query.state) {
			query = {'Address.State': req.query.state.toUpperCase()};
		}

		// zip code query
		else if (req.query.zip) {
			query = {'Address.Zip Code': req.query.zip};
		}

		// specialty query
		else if (req.query.specialty) {
			query = {'Specialization': req.query.specialty.toUpperCase()};
		}

		// no query found; returns empty map
		else {
			res.render('index', {jsonData: emptyArray});
		}

		mongoQuery(res, query);
	});
};