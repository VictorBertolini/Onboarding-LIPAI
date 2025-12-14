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