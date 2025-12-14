""" Aula 1 - Introdução à funções """

# Função é um bloco que realiza uma tarefa específica
# Dividir o problema em pequenas partes
# Evita duplicação de código

# 1. Standard Library Functions - built-in functions
# Ex: print, len

print("Olá", 123, True)

nomes = ['João', 'Maria']
tamanho_lista = len(nomes)
print(nomes, tamanho_lista)

# 2. User Defined Functions
# Definidas pelo desenvolvedor(a)
# Fazerem parte da solução do problema

# declara
# nome: suadacoes
# parametros: nenhum
# retorno: nenhum
def saudacoes():
    print("Olá")

# Chamadas
saudacoes()
saudacoes()
saudacoes()


# Declaração
# nome: saudacoes
# parametros: nome
# retorno: nenhum
def saudacoes(nome):
    print(f"Olá {nome}")

# Chamada
# valores, variáveis, expressões => argumentos
# 'Maria' é um argumento passado para o parâmetro nome
saudacoes('Maria')
saudacoes('Pedro')
nome = 'Carlos' 
saudacoes(nome)


# Declaração
# nome: calcular_media
# parametros: nota1, nota2, nota3
# retorno: nenhum
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(media)

# Chamada
# Argumentos são literais
calcular_media(10.0, 3.0, 6.0)

# Declaração
# nome: calcular_media
# parametros: nota1, nota2, nota3
# retorno: media
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

media = calcular_media(10.0, 8.4, 3.2)
print('Valor da media ', media)
# enviar no email
# salvar no banco de dados
# salvar no arquivo

