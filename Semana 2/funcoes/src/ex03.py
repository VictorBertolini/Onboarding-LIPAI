"""
Exercício 3 - Funções

Crie uma função que recebe uma tupla de números como
parâmetro (numeros) e retorna a soma desses números.
"""

def soma(tupla: tuple):
    return tupla[0] + tupla[1]

resultado = soma((5, 6))
print(resultado)

