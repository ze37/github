import './src/styles/settings/colors.css'
import './src/styles/generic/reset.css'
import './src/styles/elements/base.css'

import CardeGame from "./src/components/CardGame"

const $root = document.querySelector('#root')
const $htmlCardGame = CardeGame()
$root.insertAdjacentHTML('beforeend',$htmlCardGame)