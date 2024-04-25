import CardeGame from "../../components/CardGame"
function BoardGame(amountCards){
    //const amountCards = 3
    const $htmlCardeGame = CardeGame()
    const $htmlBoardGame = $htmlCardeGame.repeat(amountCards)
    console.log($htmlBoardGame) 
    return $htmlBoardGame   
}
export default BoardGame