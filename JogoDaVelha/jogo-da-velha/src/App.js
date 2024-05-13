import React from "react";
import "./App.css"

import Checkbox from "./object/Checkbox";
import About from "./object/About"
import Header from "./components/Header";
import Hashtag from "./components/Hashtag";
import LogoCollab from "./object/LogoCollab";
import AboutLink from "./object/AboutLink";
import IconClose from "./object/IconClose";

const App = ()=> (
    <main className="app">
      <Header />
      <Hashtag />
      <Checkbox id="show" value="show" type="checkbox" content="Mostrar eventos"/>
      <About>
        <LogoCollab />
        <AboutLink className="-light" />
        <IconClose />
      </About>


    </main> 
)


export default App;
