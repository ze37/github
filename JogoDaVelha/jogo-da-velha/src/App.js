import React from "react";
import "./App.css"

import Checkbox from "./object/Checkbox";
import Header from "./components/Header";
import Hashtag from "./components/Hashtag";

const App = ()=> (
    <main className="app">
      <Header />
      <Hashtag />
      <Checkbox id="show" value="show" type="checkbox" content="Mostrar eventos"/>
    </main> 
)


export default App;
