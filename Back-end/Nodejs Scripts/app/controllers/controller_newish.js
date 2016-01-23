module.exports = function(app) {
	app.set('json spaces', 2);
	
	// send index.html file to client
	app.get('/', function(req, res) {
		res.sendFile('index.html', {root: __dirname + '/../../public/'});
	});
	
	// route to view full mongodb dataset
	app.get('/viewall', function(req, res) {
		var docArray = [];
			
		app.locals.db.collection('testcollection').find({}, {_id: 0, 'First Name': 1, 'Last Name': 1, Specialization: 1, Address: 1}).toArray(function(err, result) {
			if (err) throw err;
			
			var i;
			
			for (i = 0; i < result.length; i++) {
				docArray.push(result[i]);
			}
			
			return res.json(docArray);
		});
	});
	
	// route to pull mongodb data via query parameters
	app.get('/search', function(req, res) {
		var state = req.query.state.toUpperCase(),
			   city = req.query.city.toUpperCase(),
			   query = {'Address.State': state, 'Address.City': city};
		
		// city & state query
		if ((city != '') && (state != '')) {
			var docArray = [];
			
			app.locals.db.collection('testcollection').find(query, {_id: 0, 'First Name': 1, 'Last Name': 1, Specialization: 1, Address: 1}).toArray(function(err, result) {
				if (err) throw err;
				
				var i;
				
				for (i = 0; i < result.length; i++) {
					docArray.push(result[i]);
				}
				
				return res.json(docArray);
				
			});
		}
		
	});
};