import React, { useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import { MarkerClusterGroup } from 'react-leaflet-markercluster'; // This imports the clustering functionality
import L from 'leaflet';

const MapWithCluster = () => {
  const [markers, setMarkers] = useState([
    { lat: 51.505, lng: -0.09, text: 'Marker 1' },
    { lat: 51.515, lng: -0.1, text: 'Marker 2' },
    { lat: 51.525, lng: -0.11, text: 'Marker 3' },
    // Add more markers if needed
  ]);

  return (
    <MapContainer center={[51.505, -0.09]} zoom={13} style={{ width: '100%', height: '500px' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&copy; OpenStreetMap contributors"
      />
      
      {/* Cluster markers */}
      <MarkerClusterGroup>
        {markers.map((marker, index) => (
          <Marker key={index} position={[marker.lat, marker.lng]}>
            <Popup>{marker.text}</Popup>
          </Marker>
        ))}
      </MarkerClusterGroup>
    </MapContainer>
  );
};

export default MapWithCluster;
