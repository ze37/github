import React from "react";
import "./style.css"
const AvatarProfile = ({src,alt})=>(
    <img className="avatar-profile" src={src} alt={alt} />
);

export default AvatarProfile