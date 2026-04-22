# Plano de Ação — Sistema Legado em Colapso

## Seção 1 — Diagnóstico

### 1. Endpoint lento (8–12s)

- Causa raiz provável:
  - Queries ineficientes (N+1, falta de índices)
  - Processamento pesado na aplicação

- Risco:
  - Experiência ruim do usuário
  - Possível perda de vendas

- Classificação:
  - Urgente e importante

---

### 2. Pedidos duplicados

- Causa raiz provável:
  - Falta de controle de idempotência
  - Problema de concorrência

- Risco:
  - Impacto financeiro direto
  - Perda de confiança do cliente

- Classificação:
  - Urgente e importante

---

### 3. Bug corrigido direto em produção

- Causa raiz provável:
  - Ausência de processo de deploy
  - Falta de cultura de versionamento

- Risco:
  - Introdução de novos bugs
  - Falta de rastreabilidade

- Classificação:
  - Importante

---

### 4. Arquivo com 4000 linhas

- Causa raiz provável:
  - Falta de modularização
  - Crescimento descontrolado do sistema

- Risco:
  - Alta dificuldade de manutenção
  - Alto risco de regressão

- Classificação:
  - Importante

---

### 5. Ausência de testes

- Causa raiz provável:
  - Falta de cultura de qualidade
  - Pressão por entrega rápida

- Risco:
  - Bugs frequentes
  - Medo de alterar código

- Classificação:
  - Urgente e importante

---

## Seção 2 — Plano de Ação

### Prioridade 1: Corrigir duplicidade de pedidos

- Ação:
  - Implementar chave única no banco (idempotência)
  - Validar requisições duplicadas
  - Adicionar controle transacional

- Esforço:
  - 1 a 2 dias

- Critério de sucesso:
  - Nenhum pedido duplicado após correção
  - Logs confirmando rejeição de duplicatas

---

### Prioridade 2: Melhorar performance do endpoint

- Ação:
  - Identificar queries lentas (profiling)
  - Criar índices no banco
  - Otimizar consultas

- Esforço:
  - 2 a 3 dias

- Critério de sucesso:
  - Tempo de resposta < 1s

---

### Prioridade 3: Introduzir testes automatizados

- Ação:
  - Criar testes unitários para regras críticas
  - Criar testes de integração básicos

- Esforço:
  - 2 a 4 dias

- Critério de sucesso:
  - Cobertura mínima das regras críticas
  - Execução automática em cada mudança

---

## Seção 3 — Decisão de Arquitetura

Escolha: Refatoração incremental

Justificativa:

- O sistema está em produção e sem testes
- Reescrita completa traz alto risco de regressão
- A refatoração incremental permite:
  - Entregas contínuas
  - Redução gradual da complexidade
  - Menor risco de quebra

Trade-off:
- Processo mais lento
- Porém muito mais seguro

---

## Seção 4 — Requisitos Não Funcionais ignorados

### 1. Desempenho

- Evidência:
  - Endpoint com 8–12 segundos

- Métrica:
  - Tempo médio de resposta < 1s

---

### 2. Confiabilidade

- Evidência:
  - Pedidos duplicados
  - Correções diretas em produção

- Métrica:
  - Taxa de erro < 1%

---

### 3. Manutenibilidade

- Evidência:
  - Arquivo com 4000 linhas
  - Ausência de testes

- Métrica:
  - Cobertura de testes > 60%
  - Tempo médio de alteração reduzido

---

## Considerações finais

O foco inicial é estabilizar o sistema:

1. Evitar prejuízo (duplicidade)
2. Melhorar experiência (performance)
3. Criar base de qualidade (testes)

Após estabilização, evoluir arquitetura gradualmente.