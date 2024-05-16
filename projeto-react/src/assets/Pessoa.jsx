import "./pessoa.css"
export const Pessoa = ({nome,idade,foto,Progamador})=>(
    <div className="pessoa">
        <img src={foto} alt="pessoa" />
        <h1>Nome: {nome}</h1>
        <p>Idade : {idade}</p>
        <p>Proficao : {Progamador}</p>
    </div>
)