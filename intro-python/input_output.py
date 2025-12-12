"""
Aula 7 - LIPAI - Entrada e Saída em Python
"""

# Saída padrão - sys stdout
print("Olá, Mundo!", "Maria")

print("Olá Mundo!", "Maria", 1, True, sep=' -> ', end=" || Final")

arquivo = open('nomes.txt', 'w', encoding='utf-8')
print("Ana", "Bruno", "Carlos", file=arquivo, sep=', ')
arquivo.close()


# Entrada 
nome = input("Digite seu nome: ")
print(nome.upper())
idade = int(input("Digite sua idade: "))

print(type(nome), type(idade))

if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, você é menor de idade.")

# file
arquivo_notas = open('notas.txt', 'r', encoding='utf-8')
conteudo = arquivo_notas.read()
notas = conteudo.split(sep=';')
print(notas)

notas = [float(nota) for nota in notas]
print(notas)

media = (notas[0] + notas[1] + notas[2]) / len(notas)

print(f"Média das notas: {media}")
arquivo_notas.close()