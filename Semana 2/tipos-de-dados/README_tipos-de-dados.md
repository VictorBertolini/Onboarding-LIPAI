# Semana 2 - Códigos

### Nome: Victor Bertolini de Sousa

### Github: https://github.com/VictorBertolini/Onboarding-LIPAI/blob/main/Semana%202

## Código das videoaulas

### Aula 1 - Listas
```python
""" Aula 1 - Tipos de Dados - Lista """

# lista 
# ordenadas
# mutáveis 
# indexáveis

nomes = ['Maria', 'Pedro', 'João', 1, True]
print(nomes, type(nomes))

print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# modificar elementos
nomes[0] = 'Maria da Silva'
nomes[1:] = ['Pedro da Silva', 'João Santos']
print(nomes)

# Tamanho de uma lista
tamanho = len(nomes)
print(tamanho)

# Adicionar elementos na lista
# métodod append
nomes.append('Marta Gomes')
print(nomes)

# método insert
nomes.insert(0, 'Guilherme Tavares')
print(nomes)

nomes.insert(2, 'Ana Lúcia')
print(nomes)

nomes2 = ['Kaio Silva', 'Carlos Gomes']
print(len(nomes))
nomes.extend(nomes2)
print(len(nomes))
print(nomes)

# Remover elementos 

# remove
nomes.remove('Maria da Silva')
print(nomes)

# del 
del nomes[0]
print(nomes)

# remove da memória
# del nomes
print(nomes) 


# nomes.clear()
print(nomes)


# iteração em lista
for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])
```
### Aula 2 - Tuplas
```python
""" Aula 2 - Tipos de Dados - Tuplas """

# tuplas
# ordenadas
# imutáveis
# indexáveis

nomes = ('Maria', 'Pedro', 'João')
print(nomes, type(nomes))

# Acessar os elementos
print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# modificar elementos (não é possível por ser imutável)
# nomes[0] = 'Maria da Silva'
# iteração

for nome in nomes:
    print(nome)

for i in range(len(nomes)):
    print(nomes[i])


print("-----")

nomes2 = 'Ana', 'Amélia', 'Marcos' 
print(nomes2, type(nomes2))

# unpack
nome1 = nomes2[0]
nome2 = nomes2[1]
nome3 = nomes2[2]

nome1, nome2, nome3 = nomes2
print(nome1, nome2, nome3)

# junção duas tuplas
todos_nomes = nomes + nomes2
print(todos_nomes, type(todos_nomes))

```
### Aula 3 - Sets
```python
""" Aula 3 - Tipos de Dados - Sets """

# tuplas
# não ordenado
# mutável
# não indexavéis
# não aceitam elementos duplicados

# criar um set
numeros = {1, 12, 5, 7, 4, 3, 3, 1}
print(numeros, type(numeros))

for numero in numeros:
    print(numero)

print(3 in numeros)
print(50 in numeros)

# adicionar itens no set
print(numeros)
numeros.add(8)
print(numeros)


# Adicionar elementos de um set em outro

print("-------")
print(numeros)
numeros2 = {1, 5, 4, 4, 3, 9}
print(numeros2)
numeros.update(numeros2)
print(numeros, type(numeros))
```
### Aula 4 - Dicionários
```python
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
```

## Código dos Exercícios
### Exercício 1
```python
""" 
Exercício 1 - Tipos de Dados

Solicite ao usuário 3 números.
Armazene os valores em uma lista.
Ao final, apresente o menor e o maior elemento.
"""
numbers = []

for i in range(3):
    num = int(input(f"Enter the {i} number: "))
    numbers.append(num)

print(f"higher Number: {max(numbers)} - Lower Number: {min(numbers)}")
```

### Exercício 2
```python
""" 
Exercício 2 - Tipos de Dados

Solicite ao usuário o mês do ano em formato numérico: 1, 2, 3, ..., 12.
Apresente o nome do mês correspondente (ex.: entrada 3 → saída == Março).
Implementar usando uma Tupla (tuple).
"""

nome_dos_meses = (
    "Janeiro",
    "Fevereiro",
    "Marco",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "outubro",
    "Novembro",
    "Dezembro"
)

numero_do_mes = int(input("Digite o número do mês desejado: "))

if 1 <= numero_do_mes <= 12:
    print(f"Mês escolhido: {nome_dos_meses[numero_do_mes - 1]}")
else:
    print("Mês inválido")
```

### Exercício 3
```python
""" 
Exercício 3 - Tipos de Dados

Solicite ao usuário o mês do ano em formato numérico: 1, 2, 3, ..., 12.
Apresente o nome do mês correspondente (ex.: entrada 3 → saída
Março).
Implementar usando um Dicionário (dict).
"""
meses = {
    1:"Janeiro",
    2:"Fevereiro",
    3:"Marco",
    4:"Abril",
    5:"Maio",
    6:"Junho",
    7:"Julho",
    8:"Agosto",
    9:"Setembro",
    10:"outubro",
    11:"Novembro",
    12:"Dezembro"
}

numero_do_mes = int(input("Digite o número do mês desejado: "))

if 1 <= numero_do_mes <= 12:
    print(f"Mês escolhido: {meses[numero_do_mes]}")
else:
    print("Mês inválido")
```
