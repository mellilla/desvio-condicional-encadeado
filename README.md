# ESTRUTURA CONDICIONAL EM PYTHON

Existe uma preocupação em Python com a indentação, com o alinhamento do código.

- Sintaxe:
tem que colocar " : " depois da condição!



# Estrutura Condicional Simples


```python

if <condição>:
    <bloco de comandos>

```

# Estrutura Condicional Composta

Existe um conjunto de comandos que devem ser executados se o teste da condição for falso ('else'):

```python

if <condição>:
    <bloco de comandos>
else:
    <bloco de comandos>

```


# OPERADORES RELACIONAIS

Quando usamos estrutura condicional, nós vamos escrever condições.
E isso traz a necessidade do uso de alguns operadores na solução de problemas que teremos que escrever a condição.

| OPERADOR RELACIONAL | DESCRIÇÃO     | EXEMPLO                |
| :-------- | :------- | :------------------------- |
| `>` | `Maior que` | 5 > 3 |
| `<` | `Menor que` | 3 < 5 |
| `>=` | `Maior igual que` | 2 >= 2 |
| `<=` | `Menor igual que` | 4 <= 4 |
| `!=` | `Diferente de` | True != False |
| `==` | `Igual a` | True == 1 |



# OPERADORES LÓGICOS

No momento da escrita de uma condição, podemos também precisar fazer uso de operadores lógicos:

| OPERADOR LÓGICO | DESCRIÇÃO     | EXEMPLO                |
| :-------- | :------- | :------------------------- |
| `NOT` | `Negação Lógica` | not True |
| `AND` | `E lógico` | True and False |
| `OR` | `OU lógico` | False or True |


# EXEMPLO DE USO

### Situação problema 1:
Faça um programa em Python para mostrar um alerta de multa quando a velocidade de um carro estiver acima do permitido (50 km/h):

#### Condicional simples:

```python
vel = float(input('Informe a velocidade em km/h: '))
if (vel > 50):
    print('Você será multado.')
    print('fim.')

```

Se for verdadeiro, o programa vai printar "você será multado" e "fim".
Do contrário, só aparecerá "fim" na mensagem.


### Situação problema 2:
Faça um programa em Python que leia um número inteiro e exiba se ele é um número par ou ímpar:

#### Condicional composta:

```python
n1 = int(input('Digite um número: '))
if n1%2 == 0:
    print('%d é um número par.' %n1)
else:
    print('%d é um número ímpar.' %n1)

```

Se n1 der resto por 2 igual a 0, ele será par.
Do contrário, é um número ímpar.



### Situação problema 3:
Escreva um programa em Python que leia dois números distintos e apresente o quadrado do maior número:

#### Condicional composta:

```python
import math

print('Digite dois números distintos: ')
n1 = float(input())
n2 = float(input())

if n1 > n2:
    quadrado = math.pow(n1, 2)
else:
    quadrado = math.pow(n2, 2)


print('Quadrado do maior número é: ', quadrado)

```

- Para resolver primeiro importa a biblioteca 'math' do Python;

- math.pow é a função de raiz quadrada;

- print final ESTÁ FORA do encadeamento, é independente de if/else.
