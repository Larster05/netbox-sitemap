// start initial ----------------------------------------------------------------------------- !

import "https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.js";

const middleOfDE = [10.4, 51];

const obj_id = document.getElementById('obj_id').value;
const map_type = document.getElementById('map_type').value;

// end initial ----------------------------------------------------------------------------- !

function get_attrctl(map_type) {
  if (map_type == "tab") {
    return true
  } else {
    return false
  }
}

function get_zoom(map_type) {
  if (map_type == "tab") {
    return 6
  } else {
    return 5.7
  }
}

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
  // request sitemap object via API
  const sitemap_obj = await getSitemap(obj_id);

  // creating map
  const map = new maplibregl.Map({
    container: "map",
    style: "/static/netbox_sitemap/styles/dark.json",
    center: middleOfDE,
    zoom: get_zoom(map_type),
    attributionControl: get_attrctl(map_type),
  });

  map.on('load', async () => {
        const image = await map.loadImage('/static/netbox_sitemap/images/marker.png');
        // Add an image to use as a custom marker
        map.addImage('custom-marker', image.data);

        map.addSource('places', {
            'type': 'geojson',
            'data': {
                'type': 'FeatureCollection',
                'features': sitemap_obj.markers
            }
        });

        // Add a layer showing the places.
        map.addLayer({
            'id': 'places',
            'type': 'symbol',
            'source': 'places',
            'layout': {
                'icon-image': 'custom-marker',
                'icon-overlap': 'always'
            }
        });

        // Create a popup, but don't add it to the map yet.
        const popup = new maplibregl.Popup({
            closeButton: false,
            offset: [0, -17],
        });

        // Make sure to detect marker change for overlapping markers
        // and use mousemove instead of mouseenter event
        let currentFeatureCoordinates = undefined;
        map.on('mousemove', 'places', (e) => {
            const featureCoordinates = e.features[0].geometry.coordinates.toString();
            if (currentFeatureCoordinates !== featureCoordinates) {
                currentFeatureCoordinates = featureCoordinates;

                // Change the cursor style as a UI indicator.
                map.getCanvas().style.cursor = 'pointer';

                const popup_coordinates = e.features[0].geometry.coordinates.slice();
                const popup_text = e.features[0].properties.name;
                const popup_url = e.features[0].properties.url;

                // Ensure that if the map is zoomed out such that multiple
                // copies of the feature are visible, the popup appears
                // over the copy being pointed to.
                while (Math.abs(e.lngLat.lng - popup_coordinates[0]) > 180) {
                    popup_coordinates[0] += e.lngLat.lng > popup_coordinates[0] ? 360 : -360;
                }

                // Populate the popup and set its coordinates
                // based on the feature found.
                popup.setLngLat(popup_coordinates).setHTML(`<strong><a href="${popup_url}" target="_blank">${popup_text}</a></strong>`).addTo(map);
            }
        });

        // Change the cursor to a pointer when the mouse is over the places layer.
        map.on('mouseenter', 'places', () => {
            map.getCanvas().style.cursor = 'pointer';
        });

        // Change it back to a pointer when it leaves.
        map.on('mouseleave', 'places', () => {
            currentFeatureCoordinates = undefined;
            map.getCanvas().style.cursor = '';
        });
    });
}

init();
