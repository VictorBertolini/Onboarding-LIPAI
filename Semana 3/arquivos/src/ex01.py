""" Exercício 1 - Arquivos 

Carregar dados de alunos. Implemente a função:
def carregar_dados_alunos(nome_arquivo):
Retorna uma tupla de dicionários com dados de
alunos.
A função deve:
■ Receber como parâmetro o nome de um arquivo que contém
dados de alunos.
■ Ler o arquivo linha a linha.
■ Para cada linha, criar um dicionário com as chaves:
● prontuario
● nome
● email
■ Retornar uma tupla, onde cada elemento é um dicionário com
os dados de um aluno.
■ Exemplo de arquivo de dados (texto):
SP000001,Maria da Silva,maria@email.com
SP000002,Pedro Gomes,pedro@email.com
SP000003,João Santos,joao@email.com
"""

def carregar_dados_alunos(nome_arquivo):
    alunos = []
    with open(nome_arquivo, 'r') as arq:
        for linha in arq:
            prontuario, nome, email = linha.strip().split(',')
            aluno = {
                'prontuario': prontuario,
                'nome': nome,
                'email': email
            }
            alunos.append(aluno)
    return tuple(alunos)

alunos = carregar_dados_alunos('Semana 3/arquivos/src/alunos.txt')


for aluno in alunos:
    print(aluno)
print(type(alunos))
