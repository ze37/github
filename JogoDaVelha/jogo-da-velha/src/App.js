import React from "react";
import Card from "./object/Card"
import Player from "./object/Player";
import Header from "./components/Header";

function App() {
  return (
  <>
    <Header />
    <Card>
      <Player player="o" />       
      <Player player="x" />
      <Player player="x" />
      
      <Player player="o" />
      <Player player="x" />
      <Player player="o" />

      <Player player="x" />
      <Player player="o" />
      <Player player="x" />

    </Card>
  </> 
  )
}

export default App;
