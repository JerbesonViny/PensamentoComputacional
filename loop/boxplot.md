## Estrutura de repetição

<p style="text-align: justify">
Para analisar dados coletados (amostras) por estudos científicos, é bastante comum o uso de boxplots, elementos gráficos que exibem os seguintes dados sobre uma amostra:
</p>

- limite superior
- limite inferior
- 1º quartil (valor que se encontra na posição 1/4 do conjunto, considerando o conjunto em ordem crescente)
- 2o quartil/mediana (valor que se encontra na metade do conjunto, considerando o conjunto em ordem crescente)
- 3º quartil (valor que se encontra na posição 3/4 do conjunto, considerando o conjunto em ordem crescente)

<p style="text-align: justify">
Nesse contexto, crie um programa que lê um conjunto de N números (N > 2). Para isso, o programa deve primeiro ler o valor de N e depois a lista de N números reais (float). Os dados devem ser informados na ordem crescente, ou seja, do menor valor para o maior, podendo haver elementos repetidos. Em seguida, o programa deve realizar a análise dos dados mostrando as informações presentes em um boxplot (limite inferior, o 1º quartil, a mediana, o 3º quartil e o limite superior), considerando o seguinte:
</p>

- Em qualquer iteração do laço de leitura dos N valores, se o valor lido for menor que o anterior, exiba a mensagem: "Erro! Conjunto tem de estar em ordem crescente" e pare o programa.
- O 1º quartil é o valor na i-ésima posição, onde i == round(N \* 1/4).
- O 3º quartil é o valor na i-ésima posição, onde i == round(N \* 3/4).
- A mediana é o elemento central dos dados. Há, porém, dois casos para o "centro". Se N for ímpar, haverá um único "elemento do meio" (ex: em [1, 3, 5], 3 é central), mas se N for par haverá dois "elementos do meio" (ex: em [1, 3, 4, 6], 3 e 4 são centrais). Nesse caso, a mediana será a média dos dois valores do meio.
- Como os dados são informados de maneira ordenada, seus valores mínimos e máximos seriam naturalmente considerados como os limites inferior e superior. Porém, o boxplot não considera valores extremos (outliers) como limites. Um valor é considerado extremo se ele está afastado da mediada por mais de 1,5 o valor do intervalo interquartílico (Terceiro Quartil – Primeiro Quartil).

### exemplo

Entrada:

```python
>>> Qual o valor do N? 7
>>> Digite os dados: 1 2 3 4 5 6 700
```

Saída:

```python
>>> Limite inferior: 1
>>> 1o quartil: 2
>>> Mediana: 4
>>> 3o quartil: 6
>>> Limite superior: 6
```
