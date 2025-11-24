// start initial ----------------------------------------------------------------------------- !

import "https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.js";

const middleOfUSA = [-100, 40];
const middleOfDE = [10, 50];

var obj_id = document.getElementById('obj_id').value;

// end initial ----------------------------------------------------------------------------- !

async function getLocation() {
  try {
    const response = await fetch("http://ip-api.com/json/");
    const json = await response.json();
    if (typeof json.lat === "number" && typeof json.lon === "number") {
      return [json.lon, json.lat];
    }
  } catch (error) {}
  return middleOfDE;
}

async function init() {
  const map = new maplibregl.Map({
    style: "/static/netbox_sitemap/styles/dark.json",
    //style: "https://tiles.openfreemap.org/styles/liberty",
    center: middleOfDE,
    zoom: 2,
    container: "map",
  });

  //const location = await getLocation();
  const location = [8.5782379168447, 49.1594315493931];
  if (location !== middleOfDE) {
    map.flyTo({ center: location, zoom: 8 });

    new maplibregl.Popup({
      closeOnClick: false,
    })
      .setLngLat(location)
      .setHTML("<h3>You are approximately here! ID: "+obj_id+"</h3>")
      .addTo(map);
  }
}

init();