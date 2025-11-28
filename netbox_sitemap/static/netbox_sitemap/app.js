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

async function getSite(site_id){
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

async function getSitesOfRegion(region_id){
  try {
    let sites_array = []

    let response = await fetch(`/api/dcim/sites/?region_id=${region_id}`);
    
    if (!response.ok){
      throw new Error(`Could not fetch region with ID ${site_id}`);
    }

    let data = await response.json();
    let sites = data.results

    for (let site of sites) {
      if (typeof site.latitude === "number" && typeof site.longitude === "number") {
        sites_array.push({"id": site.id, "latitude": site.latitude,"longitude": site.longitude, "name": site.name})
      }
    }
    return sites_array
  }
  catch (error) {
    console.error(error);
  }
}

async function getSitesOfGroup(site_group_id){
  try {
    let sites_array = []

    let response = await fetch(`/api/dcim/sites/?group_id=${site_group_id}`);
    
    if (!response.ok){
      throw new Error(`Could not fetch site_group with ID ${site_id}`);
    }

    let data = await response.json();
    let sites = data.results

    for (let site of sites) {
      if (typeof site.latitude === "number" && typeof site.longitude === "number") {
        sites_array.push({"id": site.id, "latitude": site.latitude,"longitude": site.longitude, "name": site.name})
      }
    }
    return sites_array
  }
  catch (error) {
    console.error(error);
  }
}

async function getDirectSites(sites){
  let site_objects = []
  for (let site_id of sites) {
    let site_obj = await getSite(site_id);
    if (site_obj){
      site_objects.push(site_obj);
    }
  }
  return site_objects
}

async function getRegionSites(regions){
  let site_objects = []
  for (let region_id of regions) {
    let sites_of_region = await getSitesOfRegion(region_id);
    if (sites_of_region.length !== 0){
      site_objects = site_objects.concat(sites_of_region);
    }
  }
  return site_objects
}

async function getGroupSites(site_groups){
  let site_objects = []
  for (let site_group_id of site_groups) {
    let sites_of_group = await getSitesOfGroup(site_group_id);
    if (sites_of_group.length !== 0){
      site_objects = site_objects.concat(sites_of_group);
    }
  }
  return site_objects
}

async function getAllSites(sitemap_json) {
  let all_sites = []
  const direct_sites = await getDirectSites(sitemap_json.sites)
  const region_sites = await getRegionSites(sitemap_json.regions)
  const group_sites = await getGroupSites(sitemap_json.site_groups)
  
  all_sites = all_sites.concat(direct_sites)

  for (let region_site of region_sites) {
    if (!getIdArray(all_sites).includes(region_site.id)) {
      all_sites.push(region_site);
    }
  }

  for (let group_site of group_sites) {
    if (!getIdArray(all_sites).includes(group_site.id)) {
      all_sites.push(group_site);
    }
  }

  return all_sites
}

function getIdArray(array){
  let id_array = []
  for (let object of array) {
    id_array.push(object.id)
  }
  return id_array
}

async function init() {
  const map = new maplibregl.Map({
    style: "/static/netbox_sitemap/styles/dark.json",
    //style: "https://tiles.openfreemap.org/styles/liberty",
    center: middleOfDE,
    zoom: 6,
    container: "map",
  });

  const sitemap_obj = await getSitemap_Json(obj_id);

  let sites = await getAllSites(sitemap_obj)
  console.log("all_sites")
  console.log(sites)
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

  //for (let site_obj of sites) {
  //  new maplibregl.Popup({
  //    closeOnClick: false,
  //    closeButton: false,
  //  })
  //    .setLngLat([site_obj.longitude, site_obj.latitude])
  //    .setHTML(`<strong><a href="/dcim/sites/${site_obj.id}/" target="_blank" title="Opens in a new window">${site_obj.name}</a></strong>`)
  //    .addTo(map);
  //}

  for (let site of sites) {
    new maplibregl.Marker({
      draggable: false
    })
      .setLngLat([site.longitude, site.latitude])
      .addTo(map);
  }
}

init();