title: Karte

<div id="bigmapbox"></div>
  <script src="https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.js"></script>
  <script>
    mapboxgl.accessToken = 'pk.eyJ1IjoiYWRzaGlqZiIsImEiOiJja3hwZDFjemcwOG1hMnBvMjU1aTNxYTl4In0.tyGKi8O7nFYnAYUz1Dyhsw';
    const loc = new mapboxgl.LngLat(-13.67, 13.77);
    const map = new mapboxgl.Map({
    container: 'bigmapbox', // container ID
    style: 'mapbox://styles/mapbox/satellite-streets-v11', // style URL
    center: loc,
    zoom: 4 // starting zoom
    });
    new mapboxgl.Marker({
      color: "#f0f"
    }).setLngLat(loc).addTo(map);
    map.on('load', () => {
      map.addSource('route', {
        type: 'geojson',
        data: 'https://adshijf.github.io/2021-2022/static/gps/route.geojson'
      });

      map.addLayer({
        'id': 'route',
        'type': 'line',
        'source': 'route',
        'layout': {
          'line-join': 'round',
          'line-cap': 'round'
        },
        'paint': {
          'line-color': '#f0f',
          'line-width': 6,
          'line-opacity': 0.5
        }
      });
    });
  </script>
