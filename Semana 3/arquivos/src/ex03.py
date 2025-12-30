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