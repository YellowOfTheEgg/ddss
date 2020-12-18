import React from "react";
import { AuthProvider } from "context/AuthContext";
import Routes from "./routes";
import "./app.module.scss";

function App() {
  return (
    <AuthProvider>
      <Routes />
    </AuthProvider>
  );
}

export default App;
