import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

console.log = console.warn = console.error = () => {};

ReactDOM.render(<App />, document.getElementById("root"));
