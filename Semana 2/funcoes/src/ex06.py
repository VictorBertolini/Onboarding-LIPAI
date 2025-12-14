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


