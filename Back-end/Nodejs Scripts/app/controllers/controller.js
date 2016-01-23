module.exports = function(app) {
	app.set('json spaces', 2);
	
	// route to view full mongodb dataset
	app.get('/', function(req, res) {
		var docArray = [];
			
		app.locals.db.collection('testcollection').find({}, {_id: 0, 'First Name': 1, 'Last Name': 1, Specialization: 1, Address: 1}).toArray(function(err, result) {
			if (err) throw err;
			
			for (var i = 0; i < result.length; i++) {
				docArray.push(result[i]);
			}
			
			return res.render('index', {jsonData: docArray});
		});
	});
};