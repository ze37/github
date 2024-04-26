import "./style.css"
function CardeGame (icon = "alura-pixel 1",alt = "Logo da Alura"){
    return `

        
        
        <article class="card-game">
            <img src="images/${icon}.png" alt="${alt}">
        </article>
    `;
}


export default CardeGame 