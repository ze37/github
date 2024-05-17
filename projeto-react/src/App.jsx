import { Pessoa } from "./assets/Pessoa";
import { SeyMyName } from "./assets/SeyMyName";
import { List } from "./assets/List";

export function App() {
  return (
    <main>
      <h1>Todo app</h1>
      <input type="text" />
      <button>Add</button>
      <SeyMyName nome="zeneto" />
      <Pessoa
        nome="zeneto"
        idade="40"
        Progamador="Progamador"
        foto="https://via.placeholder.com/150"
      />
      <List />
    </main>
  );
}
