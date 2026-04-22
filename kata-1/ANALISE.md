# Análise — Kata 1 (Fila de Triagem)

## Estrutura de dados escolhida

Optei por utilizar uma lista de pacientes e aplicar uma ordenação baseada em regras de prioridade.

A escolha foi feita porque:
- A entrada já é uma coleção de dados (lista)
- A ordenação pode ser resolvida com uma função de comparação (ou chave)
- Evita complexidade desnecessária de estruturas como heap ou fila de prioridade

Para calcular a prioridade, transformei as regras de negócio em um valor numérico, permitindo ordenar de forma simples e eficiente.

---

## Complexidade de tempo

A ordenação utiliza um algoritmo baseado em comparação (ex: sort do Python), com complexidade:

- Tempo: O(n log n)

Para listas pequenas ou médias, essa abordagem é suficiente.

Se a lista tivesse 1 milhão de pacientes:
- O algoritmo ainda funcionaria bem
- Porém, poderia ser otimizado utilizando uma fila de prioridade (heap), especialmente se novos pacientes forem adicionados continuamente

---

## Interação entre regras 4 e 5

Regras:

4. Idosos (60+) com urgência MÉDIA → sobem para ALTA  
5. Menores de 18 anos → ganham +1 nível de prioridade  

Caso: paciente com 15 anos e urgência MÉDIA

Passo a passo:
- Regra 5 se aplica (idade < 18)
- MÉDIA sobe para ALTA

Resultado final: ALTA

Importante:
- Regra 4 não se aplica (não é idoso)
- As regras não entram em conflito nesse caso

Observação:
Se um paciente atendesse ambas as regras (hipoteticamente), seria necessário definir uma ordem de aplicação ou consolidar regras em uma função única de prioridade.

---

## Extensibilidade (adição de novas regras)

O código foi estruturado de forma que a prioridade é calculada em uma função isolada.

Isso permite:
- Adicionar novas regras sem alterar a lógica principal de ordenação
- Manter o código organizado e de fácil manutenção

Exemplo de melhoria futura:
- Criar um sistema baseado em "regras encadeadas" (rule engine)
- Ou usar uma abordagem orientada a objetos para encapsular comportamento por tipo de paciente

---

## Considerações finais

A solução prioriza:
- Clareza de leitura
- Facilidade de manutenção
- Simplicidade na aplicação das regras

Trade-off:
- Não é a solução mais otimizada para cenários de altíssima escala em tempo real
- Porém, é adequada para o contexto proposto e facilmente evoluível