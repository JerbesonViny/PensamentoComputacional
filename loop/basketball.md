## Estrutura de repetição

<p style="text-align: justify"> 
Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques do time todo tiveram sucesso.
</p>

### Formato de entrada

<p style="text-align: justify"> 
A primeira entrada é o número de jogadores N (N >= 1). Em seguida, para cada jogador, deve-se se ler uma linha com as seguintes informações: nome do jogador, os valores S, B e A, representam a quantidade de tentativas de saques, bloqueios e ataques; os valores S1, B1 e A1, representando o número de saques, bloqueios e ataques deste jogador que tiveram sucesso.
</p>

### Formato de saída

<p style="text-align: justify"> 
A saída deve mostrar o percentual total de saques, bloqueios e ataques do time todo que resultaram em pontos, conforme mostrado no exemplo.
</p>

### Exemplo

Entrada:

```
Quantidade de jogadores? 3
Digite os dados para cada jogador:
Renan 10 20 12 1 10 9
Jonas 8 7 1 2 7 0
Edson 3 3 3 1 2 3
```

Saída:

```
As estatísticas do jogo são as seguintes:
Pontos de Saque: 19.05 %
Pontos de Bloqueio: 63.33 %
Pontos de Ataque: 75.00 %
```
