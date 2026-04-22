# Análise do Pipeline

## Decisões de tratamento

- Datas: utilizei `pd.to_datetime` com `errors="coerce"` para evitar falhas com formatos inválidos
- Valores monetários: normalizei vírgula para ponto antes de converter para float
- Cidades: normalizei para minúsculo e removi espaços
- Registros órfãos: mantive no dataset com `left join`, mas com valores nulos nas entregas
- Campos nulos: tratados com conversão segura e permitindo NaN quando necessário

## Idempotência

O pipeline é idempotente, pois:
- Não altera os arquivos de origem
- Sempre gera o mesmo resultado a partir da mesma entrada
- Não depende de estado externo

## Escalabilidade (10 milhões de linhas)

Mudanças necessárias:
- Uso de processamento em chunks (`chunksize` do pandas)
- Possível uso de PySpark ou Dask
- Armazenamento em banco de dados ao invés de CSV
- Paralelização do processamento

## Testes recomendados

- Teste de parsing de datas com múltiplos formatos
- Teste de normalização de cidades
- Teste de cálculo de atraso
- Teste de merge com registros órfãos
- Teste de valores monetários com vírgula