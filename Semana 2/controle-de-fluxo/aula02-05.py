""" Aula 05 - break e continue """

for i in range(10):
    if i == 4:
        break
    print(i)

# Encontrar a posição de um número em uma lista de inteiros
# Caso não encontre posição é igual a -1

busca = 5
numeros = [1, 4, 9, 7, 5, 3, 2, 1, 7]
posicao = -1

contador = 0
for numero in numeros:
    print("Procurando na posição: ", contador)
    if numero == busca:
        posicao = contador
        break
    contador = contador + 1

print(posicao)


for i in range(len(numeros)):
    print("Procurando na posição: ", i)
    if numeros[i] == busca:
        posicao = i
        break

# continue
# pular a iteração atual
print("----")
for numero in numeros:
    if numero == 3:
        continue        
    print(numero)
