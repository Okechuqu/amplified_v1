// ------------------------------------------------------ //
// styled Leaflet  Map
// ------------------------------------------------------ //

function map() {
    var mapId = 'map',
        mapCenter = [53.14, 8.22],
        mapMarker = true;

    if (document.getElementById(mapId)) {
        var icon = L.icon({
            iconUrl: 'img/marker.png',
            iconSize: [40, 40],
            popupAnchor: [0, -18],
            tooltipAnchor: [0, 19],
        });

        var dragging = false,
            tap = false;

        if (window.outerWidth > 700) {
            dragging = true;
            tap = true;
        }

        var map = L.map(mapId, {
            center: mapCenter,
            zoom: 12,
            dragging: dragging,
            tap: tap,
            scrollWheelZoom: false,
        });

        var Stamen_TonerLite = L.tileLayer(
            'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}{r}.{ext}',
            {
                attribution:
                    'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                subdomains: 'abcd',
                minZoom: 0,
                maxZoom: 20,
                ext: 'png',
            }
        );

        Stamen_TonerLite.addTo(map);

        map.addEventListener(
            'focus',
            function () {
                map.scrollWheelZoom.enable();
            },
            { once: true }
        );

        if (mapMarker) {
            var marker = L.marker(mapCenter, {
                icon: icon,
            }).addTo(map);

            marker
                .bindPopup(
                    `<div class="text-start p-lg-4">
                        <div class="d-flex align-items-center">
                                <div class="icon-block icon-block-lg icon-block-square">
                                    <svg class="svg-icon text-primary"><use xlink:href="#pin-1"> </use></svg>
                                </div>
                                <div class="ms-3">
                                    <h5 class="mb-0">Our main office</h5>
                                    <p class="text-sm my-0">1234 New Ave, New York, NY00235, USA</p>
                                </div>
                        </div>
                    </div>`,
                    {
                        minwidth: 200,
                        maxWidth: 400,
                        className: 'map-custom-popup',
                    }
                )
                .openPopup();
        }
    }
}

map();
