**Equipe:** Ana Carmélia e Carlos Elmen

**Disciplina:** Projeto e a Análise de Algoritmos

**Professor:** Thiago Alves Rocha


# Problema da Mochila

Problema da Mochila (*knapsack problem*) é um clássico problema de otimização, em que o objetivo é escolher um conjunto de itens, cada item possui um valor e um peso associado, para incluir na Mochila que possui uma capacidade limitada. Ou seja, a escolha deve maximizar o valor total dos itens, sem que o peso limite da mochila seja ultrapassado.

# Detalhes do Problema

Em uma mochila com capacidade limitada de peso *W*  e um conjunto de itens  *i*. Cada item i possui um valor v e peso i. O problema consiste em decidir quais itens colocar na mochila, de modo que atenda a estes requisitos:

 - O peso total dos itens selecionados não deve exceder a capacidade W.
 - O valor total dos itens selecionados deve ser o maior possível.
 
O Problema da Mochila pode ser dividido em:
 - Problema da Mochila Binária
 - Problema da Mochila com Repetição
 - Problema da Mochila Fracionária (não será abordado aqui)

## Mochila Binária Sem Repetição

Nesta versão do problema, cada item pode ser incluído na mochila apenas uma vez. Ou seja, a cada item você deve escolher:

 1. Incluir na mochila
 2. Não incluir na mochila
 
 **Formulação do Problema**
Seja:

-   Vi​: valor do  i-ésimo item.
    
-   Pi​: peso do  i-ésimo item.
    
-   W: capacidade máxima da mochila.
    
-   n: número total de itens.
    
-   dp[i][w]: valor máximo que pode ser alcançado com os primeiros  ii  itens e uma capacidade de mochila  ww.
    

A relação de recorrência é dada por:

    dp[i][w] = max(dp[i - 1][w], Vi + dp[i - 1][w-Pi])

Onde:

-   dp[i−1][w]: valor máximo sem incluir o  i-ésimo item.
    
-   Vi+dp[i−1][w−Pi]: valor máximo incluindo o  i-ésimo item (se  Pi≤w).
-   A solução ótima estará em dp[n][W].
    
 ### Exemplo

-   Itens:  [(V1=60,P1=10), (V2=100,P2=20), (V3=120,P3=30)]
    
-   Capacidade da mochila:  W=50
    
-   Solução ótima: Incluir os itens 2 e 3, com valor total  220220.

## Mochila com Repetição
Neste caso, é permitido incluir múltiplas cópias do mesmo item, desde que não exceda a capacidade da mochila.

### Formulação do Problema

Seja:

-   Vi​: valor do  i-ésimo item.
    
-   Pi​: peso do  i-ésimo item.
    
-   W: capacidade máxima da mochila.
    
-   n: número total de itens.
    
-   dp[w]: valor máximo que pode ser alcançado com uma capacidade de mochila  w.
    

A relação de recorrência é dada por:

    dp[w]=max⁡(dp[w],vi+dp[w−Pi])para todo i e w≥Pi

Onde:

-   dp[w]: valor máximo sem incluir o  i-ésimo item.
    
-   vi+dp[w−Pi]: valor máximo incluindo o  i-ésimo item (se  Pi≤w).
-   A solução ótima estará em  dp[W].

### Exemplo

-   Itens:  [(V1=60,P1=10),(V2=100,P2=20),(V3=120,P3=30)]
    
-   Capacidade da mochila:  W=50.
    
-   Solução ótima: Incluir o item 1 cinco vezes, com valor total  300.


## Diferenças entre as mochilas

| **Características** | **Mochila sem Repetição**| **Mochila com Repetição** |
| -------- | ----- | ----------- |
| Inclusão de Itens       | Cada item pode ser incluído no máximo uma vez.     | Cada item pode ser incluído múltiplas vezes.     |
| Complexidade      | O(n⋅W)    |     O(n⋅W)         |
| Aplicações      | Escolha de investimentos, seleção de projetos    |      Produção em lotes, corte de materiais.       |
| Exemplo      | Incluir itens únicos em uma mochila.     |     Incluir múltiplas cópias de um item na mochila.        |



## Links úteis
| Descrição | Link |
|--|--|
| Apresentação |  [Abrir Apresentação](https://drive.google.com/file/d/14MYV4qud4gyC0aKSwfOtst1JJ8821gb0/view?usp=sharing)
 Resultados do Trabalho|
