import { useEffect, useState } from "react";

function App() {
  const [tasks, setTasks] = useState<any[]>([]);
  const [titulo, setTitulo] = useState("");
  const [filtro, setFiltro] = useState("todas");

  const carregar = () => {
    let url = "http://127.0.0.1:8000/tasks";

    if (filtro !== "todas") {
      url += `?status=${filtro}`;
    }

    fetch(url)
      .then(res => res.json())
      .then(data => setTasks(data));
  };

  useEffect(() => {
    carregar();
  }, [filtro]);

  const criar = () => {
    if (!titulo) return;

    fetch("http://127.0.0.1:8000/tasks", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ titulo })
    })
      .then(() => {
        setTitulo("");
        carregar();
      });
  };

  const concluir = (id: number) => {
    fetch(`http://127.0.0.1:8000/tasks/${id}`, {
      method: "PATCH",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ status: "concluida" })
    }).then(carregar);
  };

  const deletar = (id: number) => {
    fetch(`http://127.0.0.1:8000/tasks/${id}`, {
      method: "DELETE"
    }).then(carregar);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Painel de Tarefas</h1>

      <input
        value={titulo}
        onChange={(e) => setTitulo(e.target.value)}
        placeholder="Nova tarefa"
      />
      <button onClick={criar}>Criar</button>

      <br /><br />

      <select onChange={(e) => setFiltro(e.target.value)}>
        <option value="todas">Todas</option>
        <option value="pendente">Pendentes</option>
        <option value="concluida">Concluídas</option>
      </select>

      <hr />

      {tasks.map((t) => (
        <div key={t.id}>
          <b>{t.titulo}</b> - {t.status}

          {t.status !== "concluida" && (
            <button onClick={() => concluir(t.id)}>Concluir</button>
          )}

          <button onClick={() => deletar(t.id)}>Deletar</button>
        </div>
      ))}
    </div>
  );
}

export default App;