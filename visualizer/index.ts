function initMap(): void {
  const map = new google.maps.Map(
    document.getElementById("map") as HTMLElement,
    {
      zoom: 12.76,
      center: { lat: 37.75, lng: -122.45 },
      mapTypeId: "terrain",
    }
  );

  fetch('sf_routes.json')
    .then(function (response) {
      return response.json();
    }).then(function (routes) {
      routes.forEach(route => {
        try {
          const routePolyline = new google.maps.Polyline({
            path: google.maps.geometry.encoding.decodePath(route['overview_polyline']['points']),
            geodesic: true,
            strokeColor: "#FF0000",
            strokeOpacity: 0.005,
            strokeWeight: 2,
          });
          routePolyline.setMap(map);
        } catch (error) {
          console.log('error ' + error + ' on route: ' + route);
        }

      });
    });
}

declare global {
  interface Window {
    initMap: () => void;
  }
}
window.initMap = initMap;
export { };
