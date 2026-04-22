from datetime import datetime

PRIORIDADES = {
    "BAIXA": 1,
    "MEDIA": 2,
    "ALTA": 3,
    "CRITICA": 4
}

def ajustar_prioridade(p):
    prioridade = PRIORIDADES[p["urgencia"]]

    # Regra 4: idoso com MÉDIA vira ALTA
    if p["idade"] >= 60 and p["urgencia"] == "MEDIA":
        prioridade = PRIORIDADES["ALTA"]

    # Regra 5: menor sobe +1 nível (sem passar de CRÍTICA)
    if p["idade"] < 18:
        prioridade = min(prioridade + 1, PRIORIDADES["CRITICA"])

    return prioridade


def ordenar_fila(pacientes):
    pacientes_processados = []

    for p in pacientes:
        novo = p.copy()
        novo["prioridade"] = ajustar_prioridade(p)
        novo["hora"] = datetime.strptime(p["horario"], "%H:%M")
        pacientes_processados.append(novo)

    return sorted(pacientes_processados, key=lambda x: (-x["prioridade"], x["hora"]))


if __name__ == "__main__":
    pacientes = [
        {"nome": "Carlos", "idade": 65, "urgencia": "MEDIA", "horario": "10:00"},
        {"nome": "Ana", "idade": 15, "urgencia": "MEDIA", "horario": "09:00"},
        {"nome": "Lucas", "idade": 10, "urgencia": "CRITICA", "horario": "11:00"},
    ]

    fila = ordenar_fila(pacientes)

    for p in fila:
        print(p["nome"], p["prioridade"])