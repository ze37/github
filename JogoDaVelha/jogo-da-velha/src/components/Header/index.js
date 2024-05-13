import React from "react";
import "./style.css"
import LogoCollab from "../../object/LogoCollab"
import AboutLink from "../../object/AboutLink" 
import Menu from "../../object/Menu"

const Header = ()=>(
    <header className="header">
        <LogoCollab />
        <AboutLink />
        <Menu />
    </header>
)
export default Header