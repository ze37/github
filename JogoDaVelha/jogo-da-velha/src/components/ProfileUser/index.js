import React from "react";
import "./style.css"
import profile from "../../object/img/zeneto.jpg"
import AvatarProfile from "../../object/AvatarProfile";
const ProfileUser = ()=>(
    <dl className="profile-user">
        <dd className="avatar">
            <AvatarProfile src={profile} alt="Avatar do zeneto"/>
        </dd>
            <dt className="title">Ze Alves</dt>
            <dd className="description">Migrei de ajudante de predeiro pra dev</dd>
    </dl>
)

export default ProfileUser