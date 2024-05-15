import React from "react";
import profile from "../../object/img/zeneto.jpg"
import AvatarProfile from "../../object/AvatarProfile";
const ProfileUser = ()=>(
    <dl>
        <dd>
            <AvatarProfile src={profile} alt="Avatar do zeneto"/>
        </dd>
            <dt>Ze Alves</dt>
            <dd>Migrei de ajudante de predeiro pra dev</dd>
    </dl>
)

export default ProfileUser