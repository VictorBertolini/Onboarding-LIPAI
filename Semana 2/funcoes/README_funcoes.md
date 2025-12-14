# Semana 2 - Códigos

### Nome: Victor Bertolini de Sousa

### Github: https://github.com/VictorBertolini/Onboarding-LIPAI/blob/main/Semana%202/

## Código das videoaulas

### Aula 1 - Introdução à funções
```python
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
```

### Aula 2 - Argumentos
```python
""" Aula 2 - Arguments: Posicional, keyword, default value """

# Declara uma função que soma dois números
def somar(n1, n2):
    return n1 + n2

def dividir(dividendo, divisor):
    return dividendo / divisor

# Argumentos posicionais 
print(somar(10.0, 3.5))
print(somar(2.0, 6.5))
print(dividir(10.0, 2.0))

# unpack list e tuplas
numeros = [10.0, 5.5]
print('somar numeros de uma lista ', somar(numeros[0], numeros[1]))
print('somar numeros de uma lista ', somar(*numeros))


# Argumentos nomeados (keyword)
print(somar(n1=3.0, n2=6.2))
print(somar(n2=5.0, n1=7.8))
print(dividir(divisor=3.0, dividendo=10.0))

# unpack dict
numeros = {
    "n1":10.2,
    "n2":5.3
}

print('somar numeros de um dict', somar(**numeros))


# Declaração
# nome: saudações:
# Parâmetros: nome (obrigatório), saudação (opcional)
# retorno: string
def saudacoes(nome, saudacao='Oi'):
    return f'{saudacao} {nome}'

print(saudacoes('João', 'Olá'))
print(saudacoes('Maria', 'Bom dia'))
print(saudacoes('Pedro'))

print(saudacoes(saudacao='Oi Oi', nome='Marcio'))
print(saudacoes(nome="Karina"))
```

## Código dos Exercícios
### Exercício 1
```python
"""
Exercício 1 - Funções

Crie uma função que recebe três números como parâmetro (n1, n2,
n3) e imprime na saída padrão a soma dos números.
"""

def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(3, 4, 5)
``` 
### Exercício 2
```python
"""
Exercício 2 - Funções

Crie uma função que recebe três números como parâmetro (n1, n2,
n3) e retorna a soma dos números.
"""

def soma(n1, n2, n3):
    return n1 + n2 + n3

resultado = soma(5, 7, 6)
print(resultado)
``` 
### Exercício 3
```python
"""
Exercício 3 - Funções

Crie uma função que recebe uma tupla de números como
parâmetro (numeros) e retorna a soma desses números.
"""

def soma(tupla: tuple):
    return tupla[0] + tupla[1]

resultado = soma((5, 6))
print(resultado)
``` 
### Exercício 4
```python
"""
Exercício 4 - Funções

Crie uma função que recebe vários argumentos numéricos através
de *args e retorna a soma dos números.
"""

def soma(*args):
    return sum(args)

resultado = soma(5, 6, 7, 8)
print(resultado)
``` 
### Exercício 5
```python
"""
Exercício 5 - Funções

Implemente uma calculadora de Índice de Massa Corporal (IMC)
usando as diretrizes da OMS. O programa deve:
○ Solicitar ao usuário seu peso (kg) e altura (m).
○ Calcular o IMC:
■ IMC = peso / (altura * altura)
■ IMC Classificação
■ -----------------------------------
■ < 18,5 Baixo peso
■ 18,5 a 24,9 Peso normal
■ 25,0 a 29,9 Excesso de peso
■ 30,0 a 34,9 Obesidade de Classe 1
■ 35,0 a 39,9 Obesidade de Classe 2
■ >= 40,00 Obesidade de Classe 3
○ Apresentar também a situação atual do indivíduo em relação ao peso
normal: "normal" , "perder peso" , "ganhar peso"
"""

def calcular_imc(individuo: dict):
    return individuo["peso"] / (individuo["altura"]**2)

def obter_classificacao(imc: float):
    if imc >= 40:
        return "Obesidade de Classe 3"
    elif imc >= 35:
        return "Obesidade de Classe 2"
    elif imc >= 30:
        return "Obesidade de Classe 1"
    elif imc >= 25:
        return "Excesso de peso"
    elif imc >= 18.5:
        return "Peso Normal"
    else:
        return "Baixo peso"
    
def situacao_individuo(imc: float):
    if imc < 18.5:
        return "Ganhar Peso"
    elif 18.5 <= imc <= 25:
        return "Normal"
    else:
        return "Perder Peso"

individuo = {
    'altura':1.79,
    'peso':78.5
}

imc = calcular_imc(individuo)
classificacao = obter_classificacao(imc)
situacao = situacao_individuo(imc)

print(f"O IMC do indivíduo é de: {imc:.2f}, sua classificação é: {classificacao} e sua situação é para {situacao}")

``` 
### Exercício 6
```python
"""
Exercício 6 - Funções

Crie um programa em Python que recebe como entrada o
comprimento, altura e largura (em cm) de um aquário e calcule:
○ O volume do aquário em litros;
○ A potência do termostato necessária para manter a temperatura adequada;
○ A quantidade de filtragem por hora (em litros) necessária para manter a
qualidade da água.
● Volume (L) = (comprimento * altura * largura) / 1000
● Potência do termostato: = volume * 0.05 * (temperatura_desejada -
temperatura_ambiente)
● Filtragem por hora: deve ser no mínimo de 2 a 3 vezes o volume do aquário.
● Requisitos:
○ Definir uma estrutura de dados para representar as entradas do usuário (por
exemplo, um dicionário com medidas e temperaturas).
○ Criar funções separadas para:
■ calcular o volume;
■ calcular a potência do termostato;
■ calcular a faixa mínima e máxima de filtragem recomendada.
○ Apresentar os resultados finais de forma organizada para o usuário.
"""

def calcula_volume(aquario: dict):
    return (aquario["comprimento"] * aquario["altura"] * aquario["largura"]) / 1000

def pontencia_do_termostato(aquario: dict):
    return calcula_volume(aquario) * 0.05 * (aquario["temp_desejada"] - aquario["temp_ambiente"])

def filtragem_por_hora(aquario: dict):
    volume = calcula_volume(aquario)
    minima = volume * 2
    maxima = volume * 3

    return (minima, maxima)



aquario = {}

comprimento = float(input("Digite o comprimento do aquário (cm): "))
altura = float(input("Digite a altura do aquário (cm): "))
largura = float(input("Digite a largura do aquário (cm): "))

temp_desejada = float(input("Digite a temperatura desejada (°C): "))
temp_ambiente = float(input("Digite a temperatura ambiente (°C): "))

aquario["comprimento"] = comprimento
aquario["altura"] = altura
aquario["largura"] = largura
aquario["temp_desejada"] = temp_desejada
aquario["temp_ambiente"] = temp_ambiente

volume = calcula_volume(aquario)
pot_termostato = pontencia_do_termostato(aquario)
faixas_filtragem = filtragem_por_hora(aquario)

print(
    f"""
====== Informações sobre o Aquário ======
O volume do aquário é: {volume}L
A pontencia do Termostato é: {pot_termostato}
As faixas de filtragem devem estar entre {faixas_filtragem[0]:.2f} e {faixas_filtragem[1]:.2f}
=========================================
"""
)
``` 

## Reflexão
### Qual função é mais flexível em relação ao uso: a do ex01 (que imprime) ou a do ex02 (que retorna o valor)? Por quê?

A mais flexível é a do ex02, dado que ela retorna o valor, o qual poderá ser utilizado em N outras aplicações, dando liberdade ao programador decidir se o resultado será usado em um outro cálculo ou salvar em algum local ou mesmo imprimir na tela. 

### Qual abordagem é mais flexível: a do ex02 (3 parâmetros fixos) ou a do ex03/ex04 (que permitem número variável de argumentos)?

A abordagem que permite um número variável de argumentos é muito mais flexível, visto que consegue se adaptar aos mais diferentes cenários e conjunto de valores, diferente do número fixo de parâmetros, que não permite utilizar nem mais e nem menos argumentos.

### As funções do ex03 e ex04 permitem enviar um número variável de parâmetros (tupla ou *args). Em que situações você prefere cada forma? Justifique.

Prefiro o uso de tupla quando adoto uma abordagem em que os parâmetros permanecem fixos ao longo do programa, partindo do princípio de que esse tipo de estrutura promove uma melhor organização do código. Embora ainda ofereça flexibilidade ao programador, a tupla impõe restrições próprias do tipo de dado `tuple`, o que contribui para maior previsibilidade e controle.
Já o uso de `*args` fornece uma liberdade máxima na definição da função, permitindo a passagem de um número arbitrário de parâmetros. Essa flexibilidade, entretanto, exige maior cuidado, especialmente em funções e aplicações mais complexas, pois demanda verificações adicionais e tratamento de possíveis erros. Ainda assim, quando utilizado de forma coerente, *args pode ser bastante útil para lidar tanto com pequenos quanto com grandes conjuntos de dados de maneira dinâmica.