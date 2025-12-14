# Semana 2 - Códigos

### Nome: Victor Bertolini de Sousa

### Github: https://github.com/VictorBertolini/Onboarding-LIPAI/blob/main/Semana%202/controle-de-fluxo/README_controle-de-fluxo.md

## Código das videoaulas

### Aula 1 - Operadores
```python
# Operadores Aritméticos
n1 = 10.2
n2 = 3.5
resultado = n1 + n2 + 8.5

print('1 + 1', 1 + 1, type(1 + 1))
print('1.2 + 1.3', 1.2 + 1.3, type(1.2 + 1.3))
print('resultado', resultado, type(resultado))

print(3-1)
print(3*2, type(3*2))
print(3/2, type(3/2))
print(3 % 2, type(3 % 2))
print(10 // 3)
print(10 ** 2)

# Operador de Atribuição
x = 10
print(x)

# Operadores de Comparação
resultado = x > 10
print(resultado, type(resultado))

print('10 == 10', 10 == 10, type(10 == 10))
print('10 != 10', 10 != 10, type(10 != 10))
print('10 > 10', 10 > 10, type(10 > 10))
print('10 >= 10', 10 >= 10, type(10 >= 10))
print('10 < 10', 10 < 10, type(10 < 10))
print('10 <= 10', 10 <= 10, type(10 <= 10))

# Operadores Lógicos
print('True and True', True and True, type(True and True))
print('True and False', True and False, type(True and False))
print('False and True', False and True, type(False and True))
print('False and False', False and False, type(False and False))

print('True or True', True or True, type(True or True))
print('True or False', True or False, type(True or False))
print('False or True', False or True, type(False or True))
print('False or False', False or False, type(False or False))

condicao = True
print('not condicao', not condicao, type(not condicao))

# Operadores Especiais

# is 
# == comparar se dois valores são iguais
# is verificar se as variáveis apontam para o mesmo objeto na memória

a = 10
b = 10.0
c = b

print(a == b, a == c, b == c)
print(a is b, a is c, b is c)


# in 
# str, list, tuple, dict 
frase = 'Você é um palavrão'

print('palavrão' in frase, type('palavrão' in frase))
print('Palavrão' in frase, type('Palavrão' in frase))

numeros = {1, 5, 2, 6}
print(10 in numeros)

pessoa = {
    'nome': 'Maria',
    'idade': 22,
    'email': 'maria@gmail.com'
}

print(22 in pessoa)
```
### Aula 2 - `if`
```python
codigo_cliente = 32
valor_desconto = 30.0
DESCONTO_ESPECIAL = valor_desconto >= 20.0

if DESCONTO_ESPECIAL:
    print("Desconto Especial")
    print(codigo_cliente)
else:
    print("Sem desconto especial")

# nome tem que ter pelo menos 3 caracteres
nome = "Lois"

print(len(nome), type(len(nome)))

NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    print("Nome deve ter pelo menos 3 caracteres")
else:
    print("Nome válido")

NOME_VALIDO = len(nome) >= 3
if NOME_VALIDO:
    print("Nome válido")
else:
    print("Nome deve ter pelo menos 3 caracteres")


if not NOME_INVALIDO:
    print("Nome válido")
else:
    print("Nome deve ter pelo menos 3 caracteres")


# nome tem que ter pelo menos 3 caracteres
# idade tem que ser maior ou igual a 18
# Exibir todos os erros no final apenas

nome = "Lo"
idade = 17
erros = []

NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    erros.append("Nome deve ter pelo menos 3 caracteres")

IDADE_INVALIDA = idade < 18
if IDADE_INVALIDA:
    erros.append("Idade deve ser maior ou igual a 18")

if len(erros) != 0:
    print(erros)
else:
    print("Dados válidos")

# False: False, None, 0, 0.0, string vazia '', lista, tuple, set vazio
# True: todo o resto
if erros:
    print(erros)
else:
    print("Dados válidos")

# if elif else

# Verifica se um número é positivo, negativo ou zero
numero = -4

# -N -4 -3 -2 -1 0 1 2 3 4 N
if numero > 0:
    print("Maior que zero")
elif numero == 0:
    print("Zero")
else:
    print("Menor que zero")

# Calcule a média e verifique se duas notas são válidas antes do cálculo
n1 = 5.6
n2 = 10.0

if n1 >= 0 and n1 <= 10:
    if n2 >= 0 and n2 <= 10:
        # media
        pass
    else:
        print("Notas inválidas")
else:
    print("Notas inválidas")


NOTA1_VALIDA = 0 <= n1 <= 10
NOTA2_VALIDA = 0 <= n2 <= 10

if NOTA1_VALIDA and NOTA2_VALIDA:
    media = (n1 + n2) / 2
    if media >= 6:
        print("Aprovado")
    elif media >= 4:
        print("Recuperação")
    else:
        print("Reprovado")
else:
    print("Notas inválidas")
```
### Aula 3 - `for`
```python
# 1. Iteração em coleção de elementos
# 2. Repetir instrução 

linguagens = ["C", "Python", "Java"]

print(linguagens[0])
print(linguagens[1])
print(linguagens[2])

# for valor in coleção:
#     # instrução
#     # instrução
#     # instrução

for linguagem in linguagens:
    print(linguagem.upper())

# Comportamento do operador in é
# diferente com base no contexto

nota1 = 10.0
nota2 = 5.5
nota3 = 8.3

media = (nota1 + nota2 + nota3) / 3
print(media)

notas = [10.0, 5.5, 8.3, 2.5]

soma = 0.0
for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print(media)

# range 
# valores = range(10)
# valores = range(0, 10)
# valores = range(0, 11, 2)
valores = range(9, -1, -1)
print(valores)

for valor in valores:
    print(valor)

for i in range(len(linguagens)):
    print(linguagens[i])
```
### Aula 4 - `while`
```python
# while condicao:
#     # instrução
#     # instrução

contador = 0
while contador <= 10:
    print(contador)
    contador += 1

print('fim')
```
### Aula 5 - `continue e break`
```python
for i in range(10):
    if i == 4:
        break
    print(i)

# Encontrar a posição de um número em uma lista de inteiros
# Caso não encontre posição é igual a -1

busca = 5
numeros = [1, 4, 9, 7, 5, 3, 2, 1, 7]
posicao = -1

contador = 0
for numero in numeros:
    print("Procurando na posição: ", contador)
    if numero == busca:
        posicao = contador
        break
    contador = contador + 1

print(posicao)


for i in range(len(numeros)):
    print("Procurando na posição: ", i)
    if numeros[i] == busca:
        posicao = i
        break

# continue
# pular a iteração atual
print("----")
for numero in numeros:
    if numero == 3:
        continue        
    print(numero)
```

## Código dos Exercícios
### Exercício 1
```python
""" 
Exercício 1 - Controle de Fluxo 

Solicite ao usuário 3 notas e apresente o resultado da média
aritmética.
"""
average = 0

for i in range(1, 4):
    average += int(input(f"Enter the {i} score: "))
    
average = average / 3
print(average)
```
### Exercício 2
```python
""" 
Exercício 2 - Controle de Fluxo 

Solicite ao usuário, uma única vez, as notas no formato n1, n2, n3,
nm e apresente:
○ a média aritmética das notas;
○ a situação: aprovado (média > 6.0), recuperação (4.0 ≤ média ≤ 6.0) ou
reprovado (média < 4.0).
"""

print("The scores must be in the format: \"n1, n2, n3, n4, ...\"")
scores = input("Enter the scores: ")

scores = scores.split(", ")
scores = list(map(lambda i: int(i), scores))

average = sum(scores) / len(scores)
print(f"Average: {average}")

if average > 6:
    print("Approved")
elif average > 4 and average < 6:
    print("Retake Exam")
else:
    print("Reproved")
```
### Exercício 3
```python
""" 
Exercício 3 - Controle de Fluxo 

Crie um programa que solicite um identificador ao usuário e
informe se é válido ou inválido
○ o código identificador contém 7 caracteres;
○ começa com BR;
○ seguido de um número inteiro entre 0001 e 9999;
○ por fim, termina com o caractere X.
○ Exemplos válidos: BR0001X, BR1236X, BR9999X
○ Exemplos inválidos: br0001X, BR126X, BR99999X, BR9999Y
"""

id = input("Enter the id: ")
correctness = 0

if len(id) == 7:
    print("Correct length")
    correctness += 1

if id.startswith("BR"):
    print("Starts with BR...")
    correctness += 1

if id.endswith("X"):
    print("Ends with X...")
    correctness += 1

num = int(id[2:-1])
if num > 0 and num < 10000:
    print(num, "Correct Middle Number")
    correctness += 1


if correctness == 4:
    print("Valid identification")
else:
    print("Invalid identification")
```
### Exercício 4
```python
"""
Exercício 4 - Controle de Fluxo 

baseado no ex03.py, ao final do programa apresente todas as
inconsistências do identificador informado (use uma list de erros).
Exemplos:
Entrada: B9999999X
Erros:
    O identificador não inicia com a sequência BR.
    O identificador não apresenta número inteiro entre 0001
    e 9999.
    ○ Entrada: BR9999Y
    Erros:
    O identificador não finaliza com o caractere X.
"""

id = input("Enter the id: ")
errors = []

if len(id) != 7:
    errors.append("The identifier does not have 7 characters.")
if not id.startswith("BR"):
    errors.append("The identifier does not start with the sequence BR.")
if not id.endswith("X"):
    errors.append("The identifier does not end with the character X.")

num = int(id[2:-1])
if 0 <= num > 9999:
    errors.append("The identifier does not have an integer number between 0001 and 9999.")

if len(errors) == 0:
    print("Valid identification")
else:
    print("Invalid identification")
    print("Errors:")
    for error in errors:
        print("-", error)
```
