import CardeGame from "../CardGame"
import "./style.css"

function CardFrontBack(icon,altIcon){
    window.cardFrontBack = {}
    window.cardFrontBack.handleClick = (event)=>{
        const $origin = event.target
        const $cardFrontBack = $origin.closest(".card-front-back")
         
        $cardFrontBack.classList.toggle("-active")
    }
    return /*html*/`
        <article class="card-front-back" onclick="cardFrontBack.handleClick(event)">
            <div class="card -front">
                ${CardeGame()}
            </div>
            <div class="card -back">
                ${CardeGame(icon,altIcon)}
            </div>    
        </article>

    `
}

export default CardFrontBack