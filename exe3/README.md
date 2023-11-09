# Exercício 3: Empréstimos

Por fim, mas não menos importante, a resolução do terceiro exercício!!! (Santander libera meu empréstimo pf 😥

## Conteúdo

- [Visão Geral](#vis%C3%A3o-geral)
- [Requisitos](#requisitos)
- [Instalação](#instala%C3%A7%C3%A3o)
- [Observações](#observa%C3%A7%C3%B5)

## Visão Geral

Este algoritmo consiste em validar valores de entrada por um usuário ficítico (nome, salário, etc) e, se sucedido, realizar a manipulação de valores para dividir um determinado número de reais em notas.
Para a validação, decidi ser ousado e converter a data de admissão inserida para um objeto da biblioteca *datetime* e aplicar a função *timedelta()*, de modo a fazer uma comparação precisa entre a data informada e a data de exatos cinco anos atrás, de modo a validar a capacidade do usuário de realizar ou não o empréstimo.
Além disso, não encontrei dificuldade em resolver a questão da fragmentação do valor em notas menores, principalmente por já ter feito um algoritmo extremamente semelhante na faculdade (para a resolução do problema [1021](https://www.beecrowd.com.br/judge/pt/problems/view/1021) do URI Online Judge em uma determinada aula)

## Requisitos

- Python 3
- [datetime](https://docs.python.org/3/library/datetime.html)
<br>Espera-se que venha junto com o pip ao instalar o Python!

## Instalação

Clone o projeto para o seu computador
```bash
$ git clone https://github.com/hyskoniho/formacao-modalgr
```
