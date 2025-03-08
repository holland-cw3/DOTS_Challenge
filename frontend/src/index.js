// index.js (new way - React 18+)
import React from 'react';
import ReactDOM from 'react-dom/client'; // Note: importing from 'react-dom/client'
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root')); // createRoot
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
