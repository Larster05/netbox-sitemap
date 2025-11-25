// start initial ----------------------------------------------------------------------------- !

import "https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.js";

const middleOfUSA = [-100, 40];
const middleOfDE = [10, 50];

const obj_id = document.getElementById('obj_id').value;

// end initial ----------------------------------------------------------------------------- !


async function getSitemap_Json(sitemap_id){
  try {
    let response = await fetch(`/api/plugins/netbox-sitemap/sitemaps/${sitemap_id}/`);
    
    if (!response.ok){
      throw new Error(`Could not fetch sitemap with ID ${sitemap_id}`);
    }

    let data = await response.json();
    return data

  }
  catch (error) {
    console.error(error);
  }
}

async function getSite_obj(site_id){
  try {
    let response = await fetch(`/api/dcim/sites/${site_id}/`);
    
    if (!response.ok){
      throw new Error(`Could not fetch site with ID ${site_id}`);
    }

    let data = await response.json();

    if (typeof data.latitude === "number" && typeof data.longitude === "number") {
      let site_json = {"id": data.id, "latitude": data.latitude,"longitude": data.longitude, "name": data.name}
      return site_json
    }

    return false

  }
  catch (error) {
    console.error(error);
  }
}

async function getSites(sites){
  let site_objects = []
  for (let site_id of sites) {
    let site_obj = await getSite_obj(site_id);
    if (site_obj){
      site_objects.push(site_obj);
    }
  }
  return site_objects
}

async function init() {
  const map = new maplibregl.Map({
    style: "/static/netbox_sitemap/styles/dark.json",
    //style: "https://tiles.openfreemap.org/styles/liberty",
    center: middleOfDE,
    zoom: 6,
    container: "map",
  });

  const obj_json = await getSitemap_Json(obj_id);
  console.log(obj_json)
  const site_objects = await getSites(obj_json.sites)
  console.log(site_objects)
  //const location = [8.5782379168447, 49.1594315493931];
  //if (location !== middleOfDE) {
  //  map.flyTo({ center: location, zoom: 8 });
  //
  //  new maplibregl.Popup({
  //    closeOnClick: false,
  //  })
  //    .setLngLat(location)
  //    .setHTML("<h3>You are approximately here! ID: "+obj_id+"</h3>")
  //    .addTo(map);
  //}

  for (let site_obj of site_objects) {
    new maplibregl.Popup({
      closeOnClick: false,
      closeButton: false,
    })
      .setLngLat([site_obj.latitude, site_obj.longitude])
//      .setHTML(`<h3>Site ${site_obj.name} is located here.</h3>`)
      .setHTML(`<strong><a href="/dcim/sites/${site_obj.id}/" target="_blank" title="Opens in a new window">${site_obj.name}</a></strong>`)
      .addTo(map);
  }
}

init();