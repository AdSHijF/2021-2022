title: Karte

<div id="bigmapbox"></div>
  <script src="https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.js"></script>
  <script>
    mapboxgl.accessToken = 'pk.eyJ1IjoiYWRzaGlqZiIsImEiOiJja3hwZDFjemcwOG1hMnBvMjU1aTNxYTl4In0.tyGKi8O7nFYnAYUz1Dyhsw';
    const map = new mapboxgl.Map({
    container: 'bigmapbox', // container ID
    style: 'mapbox://styles/mapbox/satellite-streets-v11', // style URL
    center: [-16.5,16.5], // starting position [lng, lat]
    zoom: 4 // starting zoom
    });
  </script>
