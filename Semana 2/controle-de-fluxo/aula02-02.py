""" Aula 02 - intrução if """


# if condicao:
#    # intrução
#    # intrução
# instrução

codigo_cliente = 32
valor_desconto = 30.0
DESCONTO_ESPECIAL = valor_desconto >= 20.0

if DESCONTO_ESPECIAL:
    print("Desconto Especial")
    print(codigo_cliente)
else:
    print("Sem desconto especial")


# nome tem que ter pelo menos 3 caracteres
nome = "Lois"

print(len(nome), type(len(nome)))

NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    print("Nome deve ter pelo menos 3 caracteres")
else:
    print("Nome válido")

NOME_VALIDO = len(nome) >= 3
if NOME_VALIDO:
    print("Nome válido")
else:
    print("Nome deve ter pelo menos 3 caracteres")


if not NOME_INVALIDO:
    print("Nome válido")
else:
    print("Nome deve ter pelo menos 3 caracteres")


# nome tem que ter pelo menos 3 caracteres
# idade tem que ser maior ou igual a 18
# Exibir todos os erros no final apenas

nome = "Lo"
idade = 17
erros = []

NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    erros.append("Nome deve ter pelo menos 3 caracteres")

IDADE_INVALIDA = idade < 18
if IDADE_INVALIDA:
    erros.append("Idade deve ser maior ou igual a 18")


if len(erros) != 0:
    print(erros)
else:
    print("Dados válidos")


# False: False, None, 0, 0.0, string vazia '', lista, tuple, set vazio
# True: todo o resto
if erros:
    print(erros)
else:
    print("Dados válidos")


# if elif else

# Verifica se um número é positivo, negativo ou zero
numero = -4

# -N -4 -3 -2 -1 0 1 2 3 4 N
if numero > 0:
    print("Maior que zero")
elif numero == 0:
    print("Zero")
else:
    print("Menor que zero")


# Calcule a média e verifique se duas notas são válidas antes do cálculo
n1 = 5.6
n2 = 10.0

if n1 >= 0 and n1 <= 10:
    if n2 >= 0 and n2 <= 10:
        # media
        pass
    else:
        print("Notas inválidas")
else:
    print("Notas inválidas")


NOTA1_VALIDA = 0 <= n1 <= 10
NOTA2_VALIDA = 0 <= n2 <= 10

if NOTA1_VALIDA and NOTA2_VALIDA:
    media = (n1 + n2) / 2
    if media >= 6:
        print("Aprovado")
    elif media >= 4:
        print("Recuperação")
    else:
        print("Reprovado")
else:
    print("Notas inválidas")






