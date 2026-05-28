# Problema dos Canibais e Missionarios

Este exercicio representa o classico problema dos **Canibais e Missionarios** usando uma estrutura de dados simples em Python.

O objetivo e transportar todos os canibais e missionarios do lado esquerdo para o lado direito do rio, respeitando as restricoes de seguranca.

## Objetivo

Levar:

```text
3 canibais e 3 missionarios
```

do lado esquerdo para o lado direito, usando uma canoa que pode transportar no maximo duas pessoas por viagem.

O estado inicial e:

```text
(3, 3, True)
```

E o estado final esperado e:

```text
(0, 0, False)
```

## Estrutura de dados

O estado principal do problema e representado por:

```text
(C, M, J)
```

Onde:

| Simbolo | Significado |
|---|---|
| `C` | Quantidade de canibais no lado esquerdo |
| `M` | Quantidade de missionarios no lado esquerdo |
| `J` | Posicao da jangada/canoa |

Quando `J` e `True`, a canoa esta no lado esquerdo.

Quando `J` e `False`, a canoa esta no lado direito.

## Como descobrir o lado direito

Como o total e sempre 3 canibais e 3 missionarios, o lado direito pode ser calculado assim:

```python
canibais_direita = 3 - canibais_esquerda
missionarios_direita = 3 - missionarios_esquerda
```

Exemplo:

```text
Estado: (2, 3, True)
```

Significa:

```text
Esquerda: 2 canibais, 3 missionarios
Direita:  1 canibal,  0 missionarios
Canoa:    lado esquerdo
```

## Restricoes

Para um movimento ser valido, ele precisa respeitar estas regras:

| Regra | Descricao |
|---|---|
| Maximo de 2 pessoas | A canoa leva no maximo 2 passageiros |
| Minimo de 1 pessoa | A canoa nao pode atravessar vazia |
| Seguranca dos missionarios | Canibais nao podem ser maioria onde houver missionarios |
| Posicao da canoa | So e possivel mover a canoa a partir do lado onde ela esta |
| Quantidade disponivel | Nao e possivel transportar pessoas que nao estao naquele lado |

## Operacoes disponiveis

| Operacao | Descricao |
|---|---|
| `1MD` | Transportar 1 missionario para a direita |
| `2MD` | Transportar 2 missionarios para a direita |
| `1CD` | Transportar 1 canibal para a direita |
| `2CD` | Transportar 2 canibais para a direita |
| `CMD` | Transportar 1 canibal e 1 missionario para a direita |
| `1ME` | Transportar 1 missionario para a esquerda |
| `2ME` | Transportar 2 missionarios para a esquerda |
| `1CE` | Transportar 1 canibal para a esquerda |
| `2CE` | Transportar 2 canibais para a esquerda |
| `CME` | Transportar 1 canibal e 1 missionario para a esquerda |

## Sequencia usada no teste de mesa

A solucao automatica executa a seguinte sequencia:

```text
CMD -> 1ME -> 2CD -> 1CE -> 2MD -> CME -> 2MD -> 1CE -> 2CD -> 1CE -> 2CD
```

Essa sequencia leva todos para o lado direito sem violar as regras.

## Como executar no VS Code

Abra o terminal do VS Code usando:

```text
Ctrl + `
```

Depois execute:

```powershell
py -3 .\canibais_missionarios.py
```

Se o terminal nao estiver na pasta correta, use:

```powershell
cd "C:\Users\igor\.vscode\exercicios ia\exercicio_resolucao_de_problemas"
py -3 .\canibais_missionarios.py
```

## Saida esperada

Ao executar o programa, a saida sera parecida com esta:

```text
 0. (3, 3, 1, 0, 0, 0) - CMD | valido
 1. (2, 2, 0, 1, 1, 1) - 1ME | valido
 2. (2, 3, 1, 1, 0, 0) - 2CD | valido
 3. (0, 3, 0, 3, 0, 1) - 1CE | valido
 4. (1, 3, 1, 2, 0, 0) - 2MD | valido
 5. (1, 1, 0, 2, 2, 1) - CME | valido
 6. (2, 2, 1, 1, 1, 0) - 2MD | valido
 7. (2, 0, 0, 1, 3, 1) - 1CE | valido
 8. (3, 0, 1, 0, 3, 0) - 2CD | valido
 9. (1, 0, 0, 2, 3, 1) - 1CE | valido
10. (2, 0, 1, 1, 3, 0) - 2CD | valido
11. (0, 0, 0, 3, 3, 1) | valido, Objetivo Alcancado...
```

## Arquivos do projeto

| Arquivo | Descricao |
|---|---|
| `canibais_missionarios.py` | Codigo principal com a solucao do problema |
| `README.md` | Explicacao do exercicio, regras e modo de execucao |

## Resumo

Este programa mostra como representar um problema classico de busca usando:

- tuplas;
- validacao de estados;
- regras de movimentacao;
- teste de mesa;
- execucao passo a passo.

O exercicio termina quando todos os canibais e missionarios chegam ao lado direito do rio.
