"""
Aula 6 - LIPAI - Conversão de Tipos em Python
"""

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

