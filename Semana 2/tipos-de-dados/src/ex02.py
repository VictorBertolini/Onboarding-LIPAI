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



