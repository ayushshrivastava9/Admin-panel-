// firebase-config.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.9.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.9.1/firebase-analytics.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/11.9.1/firebase-database.js";

const firebaseConfig = {
  apiKey: "YOUR_API_KEY_HERE",                 // your api key
  authDomain: "YOUR_AUTH_DOMAIN_HERE",         // your auth domain e.g. your-app.firebaseapp.com
  databaseURL: "YOUR_DATABASE_URL_HERE",      // e.g. https://your-app-default-rtdb.firebaseio.com
  projectId: "YOUR_PROJECT_ID_HERE",           // your firebase project id
  storageBucket: "YOUR_STORAGE_BUCKET_HERE",   // e.g. your-app.appspot.com
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID_HERE",
  appId: "YOUR_APP_ID_HERE",
  measurementId: "YOUR_MEASUREMENT_ID_HERE"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const db = getDatabase(app);

// Export the initialized services
export { app, analytics, db };