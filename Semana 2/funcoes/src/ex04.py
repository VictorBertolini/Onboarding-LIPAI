"""
Exercício 4 - Funções

Crie uma função que recebe vários argumentos numéricos através
de *args e retorna a soma dos números.
"""

def soma(*args):
    return sum(args)

resultado = soma(5, 6, 7, 8)
print(resultado)