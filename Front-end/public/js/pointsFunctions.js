// constructs array with doctor geolocation data
function buildPoints(data) {
  var points = [];

  for (var i = 0; i < jsonArray.length; i++) {
    points.push(L.marker([jsonArray[i].Address.Latitude, jsonArray[i].Address.Longitude]));
  }

  return points;
}

// updates markers layer and adds to cities layer
function updatePoints(points) {
  markers.addLayers(points);
  markers.addTo(doctors);
}