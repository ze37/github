import CardeGame from "../CardGame"

function CardFrontBack(){
    return /*html*/`
        <article class="card-front-back">
            ${CardeGame()}
            ${CardeGame("javascript","Logo do javascript")}
        </article>

    `
}

export default CardFrontBack