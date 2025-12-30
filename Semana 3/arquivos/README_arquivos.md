# Semana 3 - Códigos

### Nome: Victor Bertolini de Sousa

### Github: 

## Código das videoaulas

### Aula 01 - Arquivos
```python 
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
```

### Aula 02 - Arquivos
```python
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
```

## Exercícios

### Exercício 1
```python
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
``` 

### Exercício 2
```python
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
``` 

### Exercício 3
```python
"""Exercício 03 - Arquivos

Convertendo uma linha em dicionário genérico. Com base nos
códigos dos exercícios anteriores, crie a função:
def linha_para_dict(linha, chaves):
Recebe uma linha e uma lista de chaves e retorna um
dicionário.
...
A função deve receber:
■ Uma linha do arquivo (string), por exemplo: SP000001,Maria da
Silva,maria@email.com
■ Uma lista de chaves, por exemplo: ['prontuario', 'nome', 'email']
■ Exemplo 1
● Linha: SP000001,Maria da Silva,maria@email.com
● Chaves: ['prontuario', 'nome', 'email']
● Saída:
{
'prontuario': 'SP000001',
'nome': 'Maria da Silva',
'email': 'maria@email.com'
}
■ Exemplo 2
● Linha: banana,3
● Chaves: ['item', 'quantidade']
● Saída:
{
'item': 'Banana',
'quantidade': '3'
}
"""

def linha_para_dict(linha, chaves):
    valores = linha.strip().split(',')
    dicionario = {}
    for i in range(len(valores)):
        valores[i] = valores[i].strip()
        dicionario[chaves[i]] = valores[i]
    
    return dicionario

dicionario1 = linha_para_dict("SP000001,Maria da Silva,maria@email.com", ['prontuario', 'nome', 'email'])
print(dicionario1)

dicionario2 = linha_para_dict("banana,3", ['item', 'quantidade'])
print(dicionario2)
```

---

## Reflexão
# Questões do Módulo `arquivos` para serem refletidas

### Qual a vantagem de transformar cada linha do arquivo em dicionários em vez de trabalhar apenas com strings?

A vantagem clara é a organização e facilidade em encontrar uma informação dentro dos dicionários criados, trabalhar com strings tende a ser mais simples que pensar na conversão para dicionário, mas em um projeto um pouco maior e com um pouco mais de complexidade pode ser muito custoso trabalhar com os dados sem estarem organizados e sem uma facilidade em encontrar alguma informação dentro dos inúmeros dados.

### Em que situações pode ser útil retornar uma tupla de registros (como nos exercícios ex01 e ex02) em vez de apenas uma lista de linhas?


Pode ser útil quando se deseja manter os dados fixos, adicionar uma camada de segurança extra nos dados afim de que eles não sejam modificados em outra parte do código, eles são processados, "limpos" (como tirar espaços em branco ou letras maiúsculas) e depois armazenados em tuplas, as quais materão a imutabilidade deles durante o restante do programa.


### O que você achou mais desafiador: ler o arquivo ou transformar as linhas em estruturas de dados (dicionários)?

Achei mais desafiador transformar as linhas em estruturas de dados, visto que há uma necessidade de pensar a mais, enquanto ler o arquivo é um passo a passo já praticamente pré definido.