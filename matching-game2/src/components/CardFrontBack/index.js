import CardeGame from "../CardGame"

function CardFrontBack(){
    return /*html*/`
        <article class="card-front-back">
            ${CardeGame()}
            ${CardeGame()}
        </article>

    `
}

export default CardFrontBack