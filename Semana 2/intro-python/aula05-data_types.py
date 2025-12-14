"""
Aula 5 - LIPAI - Tipos de Dados em Python
"""

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
