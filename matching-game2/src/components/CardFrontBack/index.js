import CardeGame from "../CardGame"
import "./style.css"
function CardFrontBack(){
    return /*html*/`
        <article class="card-front-back">
            <div class="card -front">
                ${CardeGame()}
            </div>
            <div class="card -back">
                ${CardeGame("javascript","Logo do javascript")}
            </div>    
        </article>

    `
}

export default CardFrontBack