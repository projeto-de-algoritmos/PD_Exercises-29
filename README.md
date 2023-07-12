# Integrantes
| Nome |  Matrícula
| :------: | :-------:
| [Fernando Vargas](https://github.com/SFernandoS) | 180016491
| [Matheus Perillo](https://github.com/MatheusPerillo) | 190093421

# Introdução 
Este repositório foi criado para o desenvolvimento do segundo módulo de Programação dinâmica da disciplina Projeto de Algoritmos do Professor Maurício Serrano.

# Apresentação

[Link para a apresentação da dupla 29]() 

# Foram feitos os exercícios no LeetCode

## [416. Partition Equal Subset Sum (Medium)](https://leetcode.com/problems/partition-equal-subset-sum/description/) 

O objetivo deste problema é determinar se é possível dividir um array de números inteiros em dois subconjuntos, de forma que a soma dos elementos em cada subconjunto seja igual. A abordagem utilizada para resolver esse problema é baseada em programação dinâmica. 

![416. Partition Equal Subset Sum](/images/416.jpeg)

## [139. Word Break (Medium)](https://leetcode.com/problems/word-break/description/) 

Este exercício foi resolvido utilizando programação dinâmica. A ideia principal é construir uma tabela de memorização para verificar se cada prefixo da string pode ser formado por palavras presentes em um conjunto. A complexidade de tempo da solução típica é O(n^2), onde n é o comprimento da string.

![139. Word Break](/images/139.jpeg)

## [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/) 

Este exercício, "Cheapest Flights Within K Stops", utiliza programação dinâmica para determinar o preço mais barato para viajar de uma cidade de origem para uma cidade de destino, considerando um número máximo de paradas permitido. Através da construção de uma tabela de memorização, é verificado o custo mínimo para alcançar cada cidade, levando em conta os voos disponíveis. Caso não exista um caminho possível dentro dos critérios estabelecidos, o resultado retornado será -1.

![787. Cheapest Flights Within K Stops](/images/787.png)

## [743. Network Delay Time)](https://leetcode.com/problems/network-delay-time/description/) 

O objetivo é determinar o tempo mínimo necessário para que todos os nós recebam o sinal a partir de um nó de origem específico. O tempo de transmissão é fornecido para cada conexão entre os nós, e o problema é resolvido utilizando o algoritmo de Bellman-Ford para encontrar o caminho mais curto em um grafo ponderado direcionado. Através de iterações, o algoritmo atualiza as distâncias entre os nós até encontrar as distâncias mais curtas possíveis, levando em consideração os tempos de transmissão. Caso não seja possível que todos os nós recebam o sinal, o resultado retornado é -1.
![743. Network Delay Time](/images/743.png)
# Instalação

Pré-Requisitos: Os códigos devem ser rodados na própria plataforma do leetcode, tendo em vista o uso de uma classe Solution, bem como o uso correto dos inputs por parte da plataforma.

Caso queira rodar local, é necessário somente chamar o método da classe com os paramêtros condizente com a assinatura de acordo com a linguagem desenvolvida.

# Uso
## Passo 1: Copiar o código
Entre na pasta do exercício específico, clique no arquivo e copie-o.

## Passo 2: Entrar na página do exercício
Ao clicar no título de cada questão presente neste README, você será redirecionado para a página da questão na plataforma LeetCode

## Passo 3: Alterar linguagem
Selecione a linguagem.

## Passo 4: Colar o código
Cole o código copiado no editor.

## Passo 5: Rodar o código
Abaixo do editor de código, clique em Run para executar o código.
