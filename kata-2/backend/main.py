from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = []
id_counter = 1


@app.get("/tasks")
def listar_tasks(status: str = None):
    if status:
        return [t for t in tasks if t["status"] == status]
    return tasks


@app.post("/tasks")
def criar_task(data: dict):
    global id_counter

    if "titulo" not in data or not data["titulo"]:
        raise HTTPException(status_code=400, detail="Título obrigatório")

    task = {
        "id": id_counter,
        "titulo": data["titulo"],
        "status": "pendente"
    }

    tasks.append(task)
    id_counter += 1

    return task


@app.patch("/tasks/{task_id}")
def atualizar_task(task_id: int, data: dict):
    for t in tasks:
        if t["id"] == task_id:
            if "status" in data:
                t["status"] = data["status"]
            return t

    raise HTTPException(status_code=404, detail="Task não encontrada")


@app.delete("/tasks/{task_id}")
def deletar_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return {"ok": True}