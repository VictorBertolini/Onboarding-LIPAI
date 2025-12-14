""" Aula 1 - Tipos de Dados - Lista """

# lista 
# ordenadas
# mutáveis 
# indexáveis

nomes = ['Maria', 'Pedro', 'João', 1, True]
print(nomes, type(nomes))

print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# modificar elementos
nomes[0] = 'Maria da Silva'
nomes[1:] = ['Pedro da Silva', 'João Santos']
print(nomes)

# Tamanho de uma lista
tamanho = len(nomes)
print(tamanho)

# Adicionar elementos na lista
# métodod append
nomes.append('Marta Gomes')
print(nomes)

# método insert
nomes.insert(0, 'Guilherme Tavares')
print(nomes)

nomes.insert(2, 'Ana Lúcia')
print(nomes)

nomes2 = ['Kaio Silva', 'Carlos Gomes']
print(len(nomes))
nomes.extend(nomes2)
print(len(nomes))
print(nomes)

# Remover elementos 

# remove
nomes.remove('Maria da Silva')
print(nomes)

# del 
del nomes[0]
print(nomes)

# remove da memória
# del nomes
print(nomes) 


# nomes.clear()
print(nomes)


# iteração em lista
for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])