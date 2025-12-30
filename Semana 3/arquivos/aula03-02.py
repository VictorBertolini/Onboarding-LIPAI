""" Aula 02 - Manipulando arqs """

arq = open("Semana 3/arqs/arq.txt", "w")

# Recebe apenas string
arq.write('Hello World')

nomes = ['Caio', 'João', 'Marcos']

arq.writelines(nomes)

for nome in nomes:
    arq.write(nome + '\n')

arq.close()


with open("Semana 3/arqs/arq.txt", "r") as arq:
    arq.write('\nCaio')

with open('src/06-arqs/arq.txt', 'r') as arq:
    x = arq.read()
    print(type(x))

    x = arq.readlines() 
    print(type(x))

with open('src/06-arqs/arq.txt', 'rb') as arq: 
    x = arq.read()
    print(type(x))
    print(type(x.decode())) 

with open('src/06-arqs/arq.txt', 'r') as arq:
    print(next(arq))
    print(next(arq))

