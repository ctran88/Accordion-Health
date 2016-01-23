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
};