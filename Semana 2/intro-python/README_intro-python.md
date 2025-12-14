# Semana 2 - Códigos

### Nome: Victor Bertolini de Sousa

### Github: https://github.com/VictorBertolini/Onboarding-LIPAI/blob/main/Semana%202/intro-python/README_intro-python.md

## Código das videoaulas

### Aula 01 - Criação do projeto
```python
print("Hello World")
def somar(n1, n2):
    return n1 + n2

soma = somar(10.3, 2.5)
print(soma)
```

### Aula 02 - Identificadores
```python
# Palavras Reservadas
# True, False, None, and, as, assert, break, class, continue, def, del, elif, else, except,
# finally, for, from, global, if

# Identificadores 
# nome de variáveis, funções, classes
# Devem iniciar com letra (a-z, A-Z) ou underscore (_)
# Não podem ter espaços em branco

nome = 'LIPAI'
idade = 30

Nome = 'João'
nome_completo = 'Maria da Silva'


# Boas práticas (clean code)
c = 10
contador = 10

s = 10 + 20
soma = 10 + 20

# Constantes

PI = 3.14159

idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


MAIORIDADE = 18
if idade >= MAIORIDADE:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### Aula 03 - Comentários
```python
# Comentário de uma linha

"""
Comentário
de múltiplas 
linhas
em Python
"""

n1 = 10
n2 = 20  
soma = n1 + n2  
n3 = 30  

print(n1, n2, n3)

print(n1, n2)
print(n3)
```

### Aula 04 - Variáveis
```python
# Variável Container para guardar dados

numero = 10
print(numero, type(numero))
print(type(numero))

# Alterando o valor da variável
numero = 20
print(numero)

# Multiplas atribuições
nome, idade, endereco = 'Maria', 30, 'Rua A, 123'
print(nome, idade, endereco)


# Atribui o mesmo valor para várias variáveis 
nome1 = nome2 = nome3 = 'João'
print(nome1, nome2, nome3)

nome2 = 'Pedro'
print(nome1, nome2, nome3)

# Variáveis
# snake_case
id_funcionario = 209
salario_atual = 5000.50
print(id_funcionario, salario_atual)

# Constantes
# UPPER case - SNAKE_CASE
PI = 3.14159
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18
print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# Literais
idade = 27
print(idade)
print(27)

# Numéricos
print(10, type(10))
print(10, type(-10))
print(10.5, type(10.5))

# String
print("LIPAI", type("LIPAI"))
print("LIPAI", type("LIPAI"))
print("John's house")
print('O filme estava "excelente"!')


# Booleanos
print(True, type(True))
print(False, type(False))

# None
print(None, type(None))


# Coleções 

# Lista (list)
numeros = [1, 3, 5]
print(numeros, type(numeros))

# Tupla (tuple)
emails = ('joao@email.com', 'maria@email.com')
print(emails, type(emails))

# Conjuntos (Set)
nomes = {'Ana', 'Pedro', 'Maria'}
print(nomes, type(nomes))

# Dicionário (dictionary)
aluno = {
    'prontuario': 12345,
    'nome': 'Maria da Silva',
    'idade': 34
}
print(aluno, type(aluno))
```

### Aula 05 - Tipos de Dados
```python
# Numéricos 
# int, float

idade = 20
peso = 70.5

print(idade, type(idade))
print(peso, type(peso))

# String
nome = "Predro"
sobrenome = 'dos Santos'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

produto = 'Coca-Cola'

# O cliente nome_completo comprou o produto produto
print(f"O cliente {nome_completo} comprou o produto {produto}")

print(nome[0], nome[-1])

print(nome.lower())
print(nome.upper())

print(1, 3, 7, 10, 'Final', sep=' - ')

# boolean
ligado = True
print(ligado, type(ligado))

resultado = 10 < 3
resultado2 = 10 == 10
print(resultado, type(resultado))
print(resultado2, type(resultado2))

# Listas
frutas = ['maçã', 'banana', 'laranja']
print(frutas, type(frutas))
print(frutas[0])
print(frutas[1])
print(frutas[2])
# print(frutas[3])  # IndexError

frutas[0] = 'Maça Argentina'
frutas.append('abacaxi')

print(frutas)
print(len(frutas))

for fruta in frutas:
    print(fruta.upper())

# Tuplas
codigos = ('SP01', 'SP02', 'SP03')
print(codigos[0])

# codigos[0] = 'SP10'  # TypeError
print(len(codigos))


# Conjuntos 
resultado_sorteio = {10, 4, 3, 55, 9}
print(resultado_sorteio)

resultado_sorteio.add(18)
print(resultado_sorteio)

# Dicionários
funcionarios = {
    'codigo': 123,
    'nome': 'Ana Silva',
    'salario': 4500.00
}

print(funcionarios)
print(funcionarios['nome'])

print(funcionarios.keys())
print(funcionarios.values())

funcionarios['salario'] = 9000.00
print(funcionarios)
```

### Aula 06 - Conversão
```python
# Conversão implícita
leitura = 5.53 
peso = 3
total = leitura * peso
print(total, type(total))  

# Conversão explícita
soma = 13.4 + float('3.5')

idade = int('32')
print(idade, type(idade))

nome = 'Maria'
altura = 1.70

# mensagem = nome + ' tem ' + str(altura) + ' de altura.'
mensagem = f"{nome} tem {altura} de altura."
print(mensagem)
```

### Aula 07 - Entrada e Saída
```python
# Saída padrão - sys stdout
print("Olá, Mundo!", "Maria")

print("Olá Mundo!", "Maria", 1, True, sep=' -> ', end=" || Final")

arquivo = open('nomes.txt', 'w', encoding='utf-8')
print("Ana", "Bruno", "Carlos", file=arquivo, sep=', ')
arquivo.close()


# Entrada 
nome = input("Digite seu nome: ")
print(nome.upper())
idade = int(input("Digite sua idade: "))

print(type(nome), type(idade))

if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, você é menor de idade.")

# file
arquivo_notas = open('notas.txt', 'r', encoding='utf-8')
conteudo = arquivo_notas.read()
notas = conteudo.split(sep=';')
print(notas)

notas = [float(nota) for nota in notas]
print(notas)

media = (notas[0] + notas[1] + notas[2]) / len(notas)

print(f"Média das notas: {media}")
arquivo_notas.close()
```





