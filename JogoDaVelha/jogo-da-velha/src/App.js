import React from "react";
import "./App.css"

import Checkbox from "./object/Checkbox";
import About from "./object/About"
import AvatarProfile from "./object/AvatarProfile";
import Header from "./components/Header";
import Hashtag from "./components/Hashtag";
import HeaderInternal from "./components/HeaderInternal";
import profile from "./object/img/zeneto.jpg"

const App = ()=> (
    <main className="app">
      <Header />
      <Hashtag />
      <Checkbox id="show" value="show" type="checkbox" content="Mostrar eventos"/>
      <About>
        <HeaderInternal />
        <AvatarProfile src={profile} alt="Avatar do zeneto"/>
      </About>
    </main> 
)


export default App;
