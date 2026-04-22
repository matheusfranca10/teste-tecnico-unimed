from triagem import ordenar_fila

def test_idoso_media():
    pacientes = [
        {"nome": "Carlos", "idade": 65, "urgencia": "MEDIA", "horario": "10:00"}
    ]
    resultado = ordenar_fila(pacientes)
    assert resultado[0]["prioridade"] == 3  # ALTA


def test_menor_idade():
    pacientes = [
        {"nome": "Ana", "idade": 15, "urgencia": "MEDIA", "horario": "10:00"}
    ]
    resultado = ordenar_fila(pacientes)
    assert resultado[0]["prioridade"] == 3  # MEDIA -> ALTA


def test_menor_critica_nao_ultrapassa():
    pacientes = [
        {"nome": "Lucas", "idade": 10, "urgencia": "CRITICA", "horario": "10:00"}
    ]
    resultado = ordenar_fila(pacientes)
    assert resultado[0]["prioridade"] == 4  # continua CRÍTICA


def test_fifo_mesma_prioridade():
    pacientes = [
        {"nome": "A", "idade": 30, "urgencia": "ALTA", "horario": "09:00"},
        {"nome": "B", "idade": 25, "urgencia": "ALTA", "horario": "10:00"},
    ]
    resultado = ordenar_fila(pacientes)

    assert resultado[0]["nome"] == "A"
    assert resultado[1]["nome"] == "B"