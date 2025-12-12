"""
Aula 4 - LIPAI - Variáveis, Constantes e Literais em Python
"""

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


