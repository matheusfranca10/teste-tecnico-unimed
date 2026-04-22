# Decisões de Engenharia — Kata 2

## Arquitetura do Backend

A API foi estruturada de forma simples, seguindo princípios básicos de separação de responsabilidades:

- Camada de rota (endpoints)
- Lógica de manipulação de tarefas
- Persistência em memória (lista)

Motivação:
- Simplicidade para o contexto do teste
- Facilidade de entendimento
- Rapidez de implementação

---

## Persistência

Foi utilizada persistência em memória.

Trade-offs:
- Vantagem: simples, rápido, sem dependências
- Desvantagem: dados são perdidos ao reiniciar

Alternativas:
- SQLite (boa opção leve)
- Banco relacional (PostgreSQL)

---

## Qualidade e confiabilidade

Para tornar a API confiável em produção, eu adicionaria:

### 1. Logs estruturados
- Registro de requisições, erros e eventos importantes

### 2. Monitoramento
- Métricas de performance (tempo de resposta)
- Taxa de erros

### 3. Tratamento de erros
- Respostas HTTP consistentes (400, 404, 500)

---

## Escalabilidade (multiusuário)

Se o sistema evoluir para múltiplos usuários:

### Mudanças necessárias:

- Adicionar autenticação (JWT)
- Associar tarefas a usuários (user_id)
- Criar banco de dados real
- Separar camadas (controller, service, repository)

---

## Considerações finais

A solução prioriza simplicidade e clareza.

É adequada para:
- protótipos
- MVPs
- sistemas internos simples

Com pequenas evoluções, pode escalar para cenários reais.