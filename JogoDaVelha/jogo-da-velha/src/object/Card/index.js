import React from "react";
import "./style.css"

const Card = ({children})=>(
    <article className="card">
        {children}
    </article>

)

export default Card