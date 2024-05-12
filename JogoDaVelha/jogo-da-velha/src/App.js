import React from "react";
import "./App.css"

import Checkbox from "./object/Checkbox";
import About from "./object/About"
import Header from "./components/Header";
import Hashtag from "./components/Hashtag";
import AboutLink from "./object/AboutLink";

const App = ()=> (
    <main className="app">
      <Header />
      <Hashtag />
      <Checkbox id="show" value="show" type="checkbox" content="Mostrar eventos"/>
      <About>
        <AboutLink />
      </About>


    </main> 
)


export default App;
