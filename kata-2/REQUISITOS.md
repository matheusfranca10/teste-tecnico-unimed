# Análise de Requisitos — Painel de Tarefas

## Ambiguidades identificadas

### 1. O que define "situação" da tarefa?
- Pergunta: quais são os estados possíveis? (ex: pendente, concluída, em andamento?)
- Decisão: implementei apenas dois estados:
  - pendente
  - concluída

---

### 2. A tarefa pode ser editada após criada?
- Pergunta: posso alterar o título ou apenas o status?
- Decisão: permiti atualização parcial (PATCH), incluindo título e status

---

### 3. O filtro deve ser persistido ou apenas visual?
- Pergunta: o filtro deve ser salvo para o usuário?
- Decisão: filtro apenas no frontend (não persistente)

---

### 4. Existe identificação de usuário?
- Pergunta: o sistema é multiusuário?
- Decisão: considerei usuário único (sem autenticação)

---

## Requisitos Funcionais (RF)

- RF01: O sistema deve permitir criar uma nova tarefa
- RF02: O sistema deve listar todas as tarefas
- RF03: O sistema deve permitir marcar uma tarefa como concluída
- RF04: O sistema deve permitir excluir uma tarefa
- RF05: O sistema deve permitir filtrar tarefas por status (pendente / concluída)

---

## Requisitos Não Funcionais (RNF)

- RNF01: A API deve responder em menos de 1 segundo
- RNF02: O sistema deve ser simples e fácil de usar
- RNF03: O código deve ser organizado e legível
- RNF04: O sistema deve suportar execução local sem dependências complexas

---

## Priorização (Backlog)

O requisito de prioridade foi tratado como:

- Item de backlog futuro (não implementado agora)
- Justificativa:
  - Não é essencial para o funcionamento básico
  - Evita aumento de complexidade inicial
  - Pode ser adicionado facilmente no modelo de dados depois