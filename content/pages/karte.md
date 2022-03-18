title: Karte

<div id="bigmapbox"></div>
  <script src="https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.js"></script>
  <script>
    mapboxgl.accessToken = 'pk.eyJ1IjoiYWRzaGlqZiIsImEiOiJja3hwZDFjemcwOG1hMnBvMjU1aTNxYTl4In0.tyGKi8O7nFYnAYUz1Dyhsw';
    const loc = new mapboxgl.LngLat(-25.07, 17.03);
    const map = new mapboxgl.Map({
    container: 'bigmapbox', // container ID
    style: 'mapbox://styles/mapbox/satellite-streets-v11', // style URL
    center: loc,
    zoom: 4 // starting zoom
    });
    new mapboxgl.Marker({
      color: "#881798"
    }).setLngLat(loc).addTo(map);
    map.on('load', () => {
      map.addSource('route1', {
        type: 'geojson',
        data: 'https://adshijf.github.io/2021-2022/static/gps/2021_West_Africa.geojson'
      });
      map.addSource('route2', {
        type: 'geojson',
        data: 'https://adshijf.github.io/2021-2022/static/gps/2022_Cape_Vert.geojson'
      });
      map.addSource('flight1', {
        type: 'geojson',
        data: 'https://adshijf.github.io/2021-2022/static/gps/2022_Flights.geojson'
      });

      map.addLayer({
        'id': 'route2',
        'type': 'line',
        'source': 'route2',
        'layout': {
          'line-join': 'round',
          'line-cap': 'round'
        },
        'paint': {
          'line-color': '#881798',
          'line-width': 6,
          'line-opacity': 0.5
        }
      });

      map.addLayer({
        'id': 'route1',
        'type': 'line',
        'source': 'route1',
        'layout': {
          'line-join': 'round',
          'line-cap': 'round'
        },
        'paint': {
          'line-color': '#881798',
          'line-width': 6,
          'line-opacity': 0.5
        }
      });

      map.addLayer({
        'id': 'flight1',
        'type': 'line',
        'source': 'flight1',
        'layout': {
          'line-join': 'round',
          'line-cap': 'round'
        },
        'paint': {
          'line-color': '#0037DA',
          'line-width': 6,
          'line-opacity': 0.5
        }
      });
    });
  </script>
