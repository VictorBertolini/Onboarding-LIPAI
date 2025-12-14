""" Aula 2 - Arguments: Posicional, keyword, default value """

# Declara uma função que soma dois números
def somar(n1, n2):
    return n1 + n2

def dividir(dividendo, divisor):
    return dividendo / divisor

# Argumentos posicionais 
print(somar(10.0, 3.5))
print(somar(2.0, 6.5))
print(dividir(10.0, 2.0))

# unpack list e tuplas
numeros = [10.0, 5.5]
print('somar numeros de uma lista ', somar(numeros[0], numeros[1]))
print('somar numeros de uma lista ', somar(*numeros))


# Argumentos nomeados (keyword)
print(somar(n1=3.0, n2=6.2))
print(somar(n2=5.0, n1=7.8))
print(dividir(divisor=3.0, dividendo=10.0))

# unpack dict
numeros = {
    "n1":10.2,
    "n2":5.3
}

print('somar numeros de um dict', somar(**numeros))


# Declaração
# nome: saudações:
# Parâmetros: nome (obrigatório), saudação (opcional)
# retorno: string
def saudacoes(nome, saudacao='Oi'):
    return f'{saudacao} {nome}'

print(saudacoes('João', 'Olá'))
print(saudacoes('Maria', 'Bom dia'))
print(saudacoes('Pedro'))

print(saudacoes(saudacao='Oi Oi', nome='Marcio'))
print(saudacoes(nome="Karina"))

