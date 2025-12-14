""" 
Exercício 1 - Tipos de Dados

Solicite ao usuário 3 números.
Armazene os valores em uma lista.
Ao final, apresente o menor e o maior elemento.
"""
numbers = []

for i in range(3):
    num = int(input(f"Enter the {i} number: "))
    numbers.append(num)

print(f"higher Number: {max(numbers)} - Lower Number: {min(numbers)}")