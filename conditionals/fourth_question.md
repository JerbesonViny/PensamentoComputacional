## Condicionais

<p style="font-style: justify">
Escreva um programa que pede ao usuário um texto e dois números inteiros i1 e i2. Após lidas as entradas o programa faz as seguintes verificações:
</p>

1. Se i1 > i2 troque os valores de i1 e i2
2. Se i1 ou i2 forem maiores ou iguais ao tamanho do texto lido, finalize o programa avisando ao usuário que os valores tem que ser menores do que o tamanho do texto.

<p style="font-style: justify">
Após feitas as verificações, o programa deverá imprimir partes do texto conforme as especificações abaixo:
</p>

1. Parte 1: equivale à parte do texto que vai da primeira letra até o índice i1
2. Parte 2: equivale à parte do texto que vai da primeira letra até o índice i2
3. Parte 3: equivale à parte do texto que vai da letra de índice i1 letra até o índice i2
4. Parte 4: equivale à parte do texto que vai da letra de índice i1 até o final do texto
5. Parte 5: equivale à parte do texto que vai da letra de índice i2 até o final do texto

### Exemplos

Primeira entrada:

```
texto? teste_texto
i1? 1
i2? 5
```

Saída:

```
Partes
Parte 1: t
Parte 2: teste
Parte 3: este
Parte 4: este_texto
Parte 5: _texto
```

Segunda entrada:

```
texto? teste_texto
i1? 5
i2? 1
```

Saída:

```
Partes
Parte 1: t
Parte 2: teste
Parte 3: este
Parte 4: este_texto
Parte 5: _texto
```

Terceira entrada:

```
texto? teste_texto
i1? 1
i2? 11
```

Saída:

```
Erro! índices precisam ser menores do que o tamanho do texto (11)
```

Quarta entrada:

```
texto? Lorem ipsum dolor sit amet, consectetur adipiscing elit.
i1? 20
i2? 50
```

Saída:

```
Parte 1: Lorem ipsum dolor si
Parte 2: Lorem ipsum dolor sit amet, consectetur adipiscing
Parte 3: t amet, consectetur adipiscing
Parte 4: t amet, consectetur adipiscing elit.
Parte 5:  elit.
```
