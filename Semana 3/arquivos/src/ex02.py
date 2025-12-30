""" Exercício 2 - Arquivos

Carregar dados de projetos. Implemente a função:
def carregar_dados_projetos(nome_arquivo):
Retorna uma tupla de dicionários com dados de
projetos.
...
○ A função deve:
■ Receber como parâmetro o nome de um arquivo que contém
dados de projetos.
■ Retornar uma tupla, onde cada elemento é um dicionário com
as chaves:
● codigo – número inteiro que representa o código do
projeto
● titulo
● responsavel – nome do responsável pelo projeto
○ Assim como no exercício anterior, não utilize bibliotecas prontas para
leitura e parse do arquivo; implemente a lógica de divisão da linha em
campos.
"""

def carregar_dados_projetos(nome_arquivo):
    projetos = []
    with open(nome_arquivo, 'r') as arq:
        for linha in arq:
            codigo, titulo, responsavel = linha.strip().split(',')
            projeto = {
                'codigo': int(codigo),
                'titulo': titulo,
                'responsavel': responsavel
            }
            projetos.append(projeto)
    return tuple(projetos)

projetos = carregar_dados_projetos('Semana 3/arquivos/src/projetos.txt')
for projeto in projetos:
    print(projeto)
print(type(projetos))
