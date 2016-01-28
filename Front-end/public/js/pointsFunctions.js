// constructs array with doctor geolocation data
function buildPoints(data) {
  var points = [];

  for (var i = 0; i < jsonArray.length; i++) {
    points.push(L.marker([jsonArray[i].Address.Latitude, jsonArray[i].Address.Longitude])
        .bindPopup(
            jsonArray[i]['First Name'] + ' ' +
            jsonArray[i]['Last Name'] + '<br>' +
            jsonArray[i]['License'] + '<br>' +
            jsonArray[i]['Address']['Street_1'] + ' ' +
            jsonArray[i]['Address']['Street_2'] + '<br>' +
            jsonArray[i]['Address']['City'] + ', ' +
            jsonArray[i]['Address']['State'] + ' ' +
            jsonArray[i]['Address']['Zip Code']
        ));
  }

  return points;
}

// updates markers layer and adds to cities layer
function updatePoints(points) {
  markers.addLayers(points);
  markers.addTo(doctors);
}

// sets URL parameters depending on search type
function setUrlParam(e) {
    e.preventDefault();

    // regex to strip special characters and splits string if city, state
    var search_query = document.getElementById('tftextinput').value
      .replace(/[^\w\s]/g, '');
    var search_type = document.getElementsByName('search_res');
    var search_term = '',
        search_value = '';

    // gets search type
    for (var i = 0; i < search_type.length; i++) {
      if (search_type[i].checked) {
        search_value = search_type[i].value;
        break;
      }
    }

    // sets url search parameters
    switch (search_value) {
      case 'city':
        search_query = search_query.split(' ');
        search_term += 'city=' + search_query[0] + '&state=' + search_query[1];
        break;
      case 'state':
        search_term += 'state=' + search_query;
        break;
      case 'zip':
        search_term += 'zip=' + search_query;
        break;
      case 'specialty':
        search_term += 'specialty=' + search_query;
        break;
    }

    window.location.href = 'search?' + search_term;
}