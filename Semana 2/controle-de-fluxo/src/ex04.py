"""
Exercício 4 - Controle de Fluxo 

baseado no ex03.py, ao final do programa apresente todas as
inconsistências do identificador informado (use uma list de erros).
Exemplos:
Entrada: B9999999X
Erros:
    O identificador não inicia com a sequência BR.
    O identificador não apresenta número inteiro entre 0001
    e 9999.
    ○ Entrada: BR9999Y
    Erros:
    O identificador não finaliza com o caractere X.
"""

id = input("Enter the id: ")
errors = []

if len(id) != 7:
    errors.append("The identifier does not have 7 characters.")
if not id.startswith("BR"):
    errors.append("The identifier does not start with the sequence BR.")
if not id.endswith("X"):
    errors.append("The identifier does not end with the character X.")

num = int(id[2:-1])
if 0 <= num > 9999:
    errors.append("The identifier does not have an integer number between 0001 and 9999.")

if len(errors) == 0:
    print("Valid identification")
else:
    print("Invalid identification")
    print("Errors:")
    for error in errors:
        print("-", error)
