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
