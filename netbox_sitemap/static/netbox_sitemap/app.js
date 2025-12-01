// start initial ----------------------------------------------------------------------------- !

import "https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.js";

const middleOfUSA = [-100, 40];
const middleOfDE = [10, 50];

const obj_id = document.getElementById('obj_id').value;

// end initial ----------------------------------------------------------------------------- !

async function getSitemap(sitemap_id){
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

async function init() {
  const map = new maplibregl.Map({
    style: "/static/netbox_sitemap/styles/dark.json",
    //style: "https://tiles.openfreemap.org/styles/liberty",
    center: middleOfDE,
    zoom: 6,
    container: "map",
  });

  const sitemap_obj = await getSitemap(obj_id);

  const geojson = {
	  'type': 'FeatureCollection',
	  'features': sitemap_obj.markers
	};
  console.log(geojson)

  // add markers to map
  geojson.features.forEach((marker) => {
    // create a DOM element for the marker
    const el = document.createElement('div');
    el.className = 'marker';
    el.style.backgroundImage = "url(/static/netbox_sitemap/images/branch.png)";
    el.style.backgroundPosition = "center center";
    el.style.backgroundRepeat = "no-repeat"
    el.style.width = `${marker.properties.iconSize[0]}px`;
    el.style.height = `${marker.properties.iconSize[1]}px`;

    el.addEventListener('click', () => {
      window.alert(marker.properties.name);
    });

    // add marker to map
    new maplibregl.Marker({element: el})
      .setLngLat(marker.geometry.coordinates)
      .addTo(map);
    });

}

init();
