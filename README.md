# Teste Técnico — Unimed Caruaru

## Nome

Felipe Matheus da Silva França

## Telefone

81991301474
81996900444

## E-mail

matheus19961@outlook.com

---

## Stack(s) utilizada(s) e justificativa

### Backend — Python (FastAPI)

Utilizei FastAPI por permitir criação rápida de APIs, com boa performance e código simples de manter.

### Frontend — React + TypeScript (Vite)

Escolhi React com TypeScript para garantir melhor organização, tipagem e escalabilidade. O Vite foi usado pela rapidez no ambiente de desenvolvimento.

### Dados — Python (Pandas)

Utilizei Pandas para o pipeline de dados por ser eficiente na manipulação, limpeza e transformação de arquivos CSV.

---

## Como executar cada kata

### Kata 1 — Fila de Triagem

cd kata-1
python main.py

---

### Kata 2 — Painel de Tarefas

#### Backend

cd kata-2/backend
pip install fastapi uvicorn
uvicorn main:app --reload

A API estará disponível em:
http://127.0.0.1:8000

---

#### Frontend

cd kata-2/frontend
npm install
npm run dev

A aplicação estará disponível em:
http://localhost:5173

---

### Kata 3 — Análise

Arquivo:
kata-3/PLANO.md

---

### Kata 4 — Pipeline de Dados

cd kata-4
pip install pandas
python pipeline.py

Será gerado o arquivo:
consolidado.csv

---

## Comentários finais

Se tivesse mais tempo, eu:

- Revisaria melhor o código para deixá-lo mais organizado e legível
- Validaria mais cenários de entrada para evitar possíveis erros
- Melhoraria a experiência de uso da interface
- Testaria mais o sistema para garantir que todas as funcionalidades estão funcionando corretamente
