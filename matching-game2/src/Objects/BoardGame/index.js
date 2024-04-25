import "./style.css"
import CardeGame from "../../components/CardGame"
function BoardGame(amountCards){
    const $htmlCardeGame = CardeGame()
    const $htmlContent = $htmlCardeGame.repeat(amountCards)
    
    return /*html*/`
        <section class="board-game">
            ${$htmlContent}
        </section>
        `
}
export default BoardGame