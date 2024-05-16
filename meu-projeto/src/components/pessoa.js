import React from "react";

function Pessoa({nome,idade,foto,proficao}){
    return (
        <div>
            <img src={foto} alt="props.nome"/>
            <h2>Nome: {nome}</h2>
            <p>idade: {idade}</p>
            <p>Proficao: {proficao}</p>
        </div>
    )
}

export default Pessoa