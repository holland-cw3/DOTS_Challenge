"use client";

import {
  APIProvider,
  Map,
  useMap,
  AdvancedMarker,
} from "@vis.gl/react-google-maps";
import { MarkerClusterer } from "@googlemaps/markerclusterer";
import type { Marker } from "@googlemaps/markerclusterer";
import React, { useState, useEffect, useRef } from "react";
import polka from "./data/polka";

type Props = {
  lots: string[];  // Array of lot names to filter by
};

const MyComponent: React.FC<Props> = ({ lots }) => {
  // Filter the polka array based on the lots names
  const filteredPolka = polka.filter(p => lots.includes(p.name));

  return (
    <div style={{ height: "100vh", width: "100%" }}>
      <APIProvider apiKey="AIzaSyAwAvjnjdwbdVNWZEFrAt9iXbjt_UTtoIc">
        <Map
          center={{ lat: 38.9888, lng: -76.948 }} 
          zoom={15.2}
          mapId="dff3354deffa427c"
        >
          <Markers points={filteredPolka} />
        </Map>
      </APIProvider>
    </div>
  );
};

type Point = google.maps.LatLngLiteral & { key: string };
type MarkersProps = { points: Point[] };

const Markers = ({ points }: MarkersProps) => {
  const map = useMap();
  const [markers, setMarkers] = useState<{ [key: string]: Marker }>({});
  const clusterer = useRef<MarkerClusterer | null>(null);

  useEffect(() => {
    if (!map) return;
    if (!clusterer.current) {
      clusterer.current = new MarkerClusterer({ map });
    }
  }, [map]);

  useEffect(() => {
    clusterer.current?.clearMarkers();
    clusterer.current?.addMarkers(Object.values(markers));
  }, [markers]);

  const setMarkerRef = (marker: Marker | null, key: string) => {
    if (marker && markers[key]) return;
    if (!marker && !markers[key]) return;

    setMarkers((prev) => {
      if (marker) {
        return { ...prev, [key]: marker };
      } else {
        const newMarkers = { ...prev };
        delete newMarkers[key];
        return newMarkers;
      }
    });
  };

  return (
    <>
      {points.map((point) => (
        <AdvancedMarker
          position={point}
          key={point.key}
          ref={(marker) => setMarkerRef(marker, point.key)}
        >
          <span style={{ fontSize: "2rem" }}>🟡</span>
        </AdvancedMarker>
      ))}
    </>
  );
};

export default MyComponent;
