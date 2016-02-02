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

	// function to change state names to abbreviations
	function stateAbbr(input) {
		var states = [
		        ['arizona', 'AZ'],
		        ['alabama', 'AL'],
		        ['alaska', 'AK'],
		        ['arizona', 'AZ'],
		        ['arkansas', 'AR'],
		        ['california', 'CA'],
		        ['colorado', 'CO'],
		        ['connecticut', 'CT'],
		        ['delaware', 'DE'],
		        ['florida', 'FL'],
		        ['georgia', 'GA'],
		        ['hawaii', 'HI'],
		        ['idaho', 'ID'],
		        ['illinois', 'IL'],
		        ['indiana', 'IN'],
		        ['iowa', 'IA'],
		        ['kansas', 'KS'],
		        ['kentucky', 'KY'],
		        ['kentucky', 'KY'],
		        ['louisiana', 'LA'],
		        ['Maine', 'ME'],
		        ['maryland', 'MD'],
		        ['massachusetts', 'MA'],
		        ['michigan', 'MI'],
		        ['minnesota', 'MN'],
		        ['mississippi', 'MS'],
		        ['missouri', 'MO'],
		        ['montana', 'MT'],
		        ['nebraska', 'NE'],
		        ['nevada', 'NV'],
		        ['new hampshire', 'NH'],
		        ['new jersey', 'NJ'],
		        ['new mexico', 'NM'],
		        ['new york', 'NY'],
		        ['north carolina', 'NC'],
		        ['north dakota', 'ND'],
		        ['ohio', 'OH'],
		        ['oklahoma', 'OK'],
		        ['oregon', 'OR'],
		        ['pennsylvania', 'PA'],
		        ['rhode island', 'RI'],
		        ['south carolina', 'SC'],
		        ['south dakota', 'SD'],
		        ['tennessee', 'TN'],
		        ['texas', 'TX'],
		        ['utah', 'UT'],
		        ['vermont', 'VT'],
		        ['virginia', 'VA'],
		        ['washington', 'WA'],
		        ['west virginia', 'WV'],
		        ['wisconsin', 'WI'],
		        ['wyoming', 'WY'],
		    ];

		input = input.replace(/\w/g, function(txt){return txt.toLowerCase();});
		for (var i = 0; i < states.length; i++) {
			if (states[i][0] == input) {
				return (states[i][1]);
				break;
			}
		}

		return input;
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
		var state = '';

		// city query
		if (req.query.city && req.query.state) {
			state = stateAbbr(req.query.state).toUpperCase();
			query = {'Address.City': req.query.city.toUpperCase(), 'Address.State': state};
		}

		// state query
		else if (req.query.state) {
			state = stateAbbr(req.query.state).toUpperCase();
			query = {'Address.State': state};
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