import React from "react";
import "./style.css"
import playerX from "../img/X.png"
import playerO from "../img/O.png"

const Player = ({player})=>{
   const players = []
   players["x"] = playerX
   players["o"] = playerO
   return (<button className="player">
        <img src={players[player]} alt={`jogador ${player.toUpperCase()}`}/>
    </button>)
}

export default Player