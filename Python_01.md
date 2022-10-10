# Python Aula 01

## Objetivos Iniciais do Python

- Linguagem fácil e intuitiva
- Código aberto
- Inteligivel em inglês
- Adequada para tarefas diarias e que fosse produtiva

## Versátil

- Tipagem dinâmica e forte (não precisa definir o tipo) (nao deixa fazer operações entre tipos diferentes)
- Miltiplataforma e multiparadigma (Win,Mac,Linux)
- Comunidade grande e ativa
- Curva de aprendizado baixa

Evitar utilizar para desenvolvimento mobile

## Dicas

modo interativo, para usar basta digitar python no terminal

help(lista a documentação do método) e dir(mostra os métodos do objeto)

forma de fazer variavel constante py:
nome em MAIUSCULO significa imutabilidade da variavel

## Conversão de tipos

utilizando flot(valor a ser convertido), int(valor a ser convertido)

conversão por divisão (10/1), (10/2)

str(valor a ser convertido)

f" frase {valor a ser contatenado} frase {ou variavel}"

## Erro de Conversão

caso não for possivel apresentará erro

## Funções de entrada e saída

input para receber valores

print para exibir

end para definir o final da informação exibida (nome, end="...")

sep muda o separador entre as variaveis (nome, valor, sep="#")

## Operadores Aritméticos

soma + 
subtração -
multiplicação *
divisão /, divisão inteira //

mudulo (resto da divisão) %
elevação ou exponeciação **

precedebcia dos operadores
() parentesis
(*) expoentes
multiplicação e divisão (esquerda pra direita)
soma e subtração (esquerda pra direita)

## Operadores de comparação

== igualdade
=! diferente

 a > ou >= maior ou maior ou igual
 a < ou <= menor ou menor ou igual

 ## Operadores de atribuição

 utilizados para definir o valor de uma variavel

 = atribuição simples (var = valor)
 += adição mais a variavel (var+= 10)
 -= subtração menos a variavel (var -=10)
 *= multiplicação pela variavel (var *=10)
 /* divisão pela variavel (var /=10)
 //* divisão inteira pela variavel (var //=10)
 %= modulo pela variavel (var %=10)
 **= exponenciação pela varival (var **=10)

## Operadores lógicos

Retorna um valor booleano como resultado de uma expressão
 
 and a totalidade da operação deve ser verdade para reornar true, caso parte ou a totalidade das operações sejam falsas retorna false.

 or uma das operações devem ser verdadeiras para retornar true, caso a totalidade seja falsa retorna false

 not inverte o valor boleano resultante , !false = true

Precedencia 
preferencia por usar parenteses para organizar a ordem de execução

## Operadores de identidade

Operador para saber se as variaveis ocupam a mesma posição ná mémoria

is / is not

## Operadores de Associação

Operadores utilizados para verificar se objetos estão em uma sequencia

in / not in

## identação e Blocos

Além de facilitar a leitura e a manuteção
Serve para definir os blocos de comando inicia e termina

: inicia o bloco de comando

usar 4 espaços em branco para identar ----

## Manipulação de Strings

### Maiusculo e Minusculo

métodos úteis em strings
upper transforam em maiusculo
lower transforma em minusculo
title primeira letra em maiuscula e reto em minusculo

### Espaço em branco

strip retira espaços em branco das strings
lstrip retira espaços da esquerda left strip =lstrip
rstrip retira espaços da direita right strip =lstrip

### Junções e Centralizações

center centraliza a string de acordo com os parametros de tamanho e caractere para completar (10,&) ou (6, )
join serve como separador da palavra ".".join("Jose")

## Interpolação de váriavel

f strings deve ser priorizada

%tipodastring %s string %d inteiros e %f float 
depois passa o argumento % e entre parentesis as variaveis (idade, nome)

format {} em vez de % ao final aciona o metodo .format e passa as variaveis (nome, idade) pode passar a posição da variavel escolhida entre as {}.
ex: {1} {0} (nome, idade) 21 josé

também pode passar o nome da variavel dentro do acionamento do metodo definir as variaveis
ex: .format(nome=nome, idade=idade)

ou pode passar dicionario .format(**pessoa)

### F-string

parecido com o format entre as chaves já passa o nome da variavel f" Ola sou o {nome}, tenho {idade} anos"

formatação {PI:.2f} mostra somente duas casas decimais
{PI:10.3f} 10 espaços para frente e 2 decimais

## Fatiamento de Strings
tratamos como um vetor
nome[0] primeiro elemento do nome
nome[:9] retorna até 8 elemento
    [10:] a partir do 10 elemento até o fim
    [10:16] inicio e fim
    [10:16:2] pula dois caracteres como o passo
    [::-1] irá inverter a string