import React from "react";
import "./style.css"

import LogoCollab from "../../object/LogoCollab";
import AboutLink from "../../object/AboutLink";
import IconClose from "../../object/IconClose";

const HeaderInternal = ()=>(
    <header className="header-internal">
        <LogoCollab light />
        <AboutLink className="-light" />
        <IconClose />

    </header>
)

export default HeaderInternal