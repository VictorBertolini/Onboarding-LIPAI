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