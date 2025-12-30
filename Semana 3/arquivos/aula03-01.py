# open("caminho", "r")

# Mode
# r - leitura
# a - Append \ Incrementar
# w - escrita (apaga o conteúdo anterior)
# x - cria um arquivo
# r+

arquivo = open("Semana 3/arquivos/test.txt", "a")

# print(arquivo.readable())

# print(arquivo.read())

# print(arquivo.readline())

# lista = arquivo.readlines()

# print(lista)

# print(lista[3])

# arquivo.write("\nC")
# arquivo.write("\nC++")
# arquivo.write("\nTerraform")

# arquivo.close()

import os


# if os.path.exists("Semana 3/arquivos/test.txt"):
#     os.remove("Semana 3/arquivos/test.txt")
# else:
#     print("O arquivo não existe")

os.rmdir("Semana 3/arquivos/nova_pasta")

