// constructs array with doctor geolocation data
function buildPoints(data) {
  var points = [];

  for (var i = 0; i < jsonArray.length; i++) {
    points
      .push(L.marker([jsonArray[i].Address.Latitude, jsonArray[i].Address.Longitude])
      .bindPopup(
        jsonArray[i]['First Name'] + ' ' +
        jsonArray[i]['Last Name'] + "<br>" +
        jsonArray[i]['Specialization'] + "<br>" +
        jsonArray[i]['Address']['Street_1'] + ' ' +
        jsonArray[i]['Address']['Street_2'] + "<br>" +
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