""" Aula 4 - Tipos de Dados - Dics """

# dic (dicionários)
# coleção de key-value (chave-valor)
# ley ela é única 
# mutável

# Criar um dic
carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}

# Acessar valores
print(carro, type(carro))
print(carro["marca"])
print(carro.get("marca"))

# Pegar todas as chaves, valores, pares
print(carro.keys())
print(carro.values())
print(carro.items())


# Verificar se uma chave existe
print("marca" in carro)
print("cor" in carro)

# Adicionar chave/valor de forma dinânmica
carro["cor"] = "Azul"
print("cor" in carro)
print(carro, type(carro))

# Remove a chave
marca = carro.pop("marca")
print(marca)
print(carro)

# loop
for key in carro:
    print(key, carro[key], type(key))

for value in carro.values():
    print(value)

for key in carro.keys():
    print(key)

print(carro.items())

for key, value in carro.items():
    print(key, value)

# Lista de dicionários
aluno1 = {
    "nome": "João",
    "email": "joão@email.com",
    "notas": [10.0, 5.3, 7.0]
}

aluno2 = {
    "nome": "Maria",
    "email": "maria@email.com",
    "notas": [10.0, 2.3, 10.0]
}

alunos = [aluno1, aluno2]

for aluno in alunos:
    print(aluno['nome'], aluno['email'])
    for nota in aluno['notas']:
        print(nota)