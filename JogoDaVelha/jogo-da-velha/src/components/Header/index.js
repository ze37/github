import React from "react";
import "./style.css"
import Logo from "../../object/Logo"
import AboutLink from "../../object/AboutLink" 
import Menu from "../../object/Menu"

const Header = ()=>(
    <header className="header">
        <Logo />
        <AboutLink />
        <Menu />
    </header>
)
export default Header