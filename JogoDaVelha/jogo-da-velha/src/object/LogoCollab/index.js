import React from "react";
//import "./style.css"
import CollabCode from "../img/foto.png";
import CollabCodeLight from "../img/colabe.png"

const LogoCollab = ({light = false})=>(
    <img className="logo-collab" 
        src={light ? CollabCodeLight : CollabCode} 
        alt="Logo do projeto"
    />
)
export default LogoCollab