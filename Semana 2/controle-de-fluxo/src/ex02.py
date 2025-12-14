""" 
Exercício 2 - Controle de Fluxo 

Solicite ao usuário, uma única vez, as notas no formato n1, n2, n3,
nm e apresente:
○ a média aritmética das notas;
○ a situação: aprovado (média > 6.0), recuperação (4.0 ≤ média ≤ 6.0) ou
reprovado (média < 4.0).
"""

print("The scores must be in the format: \"n1, n2, n3, n4, ...\"")
scores = input("Enter the scores: ")

scores = scores.split(", ")
scores = list(map(lambda i: int(i), scores))

average = sum(scores) / len(scores)
print(f"Average: {average}")

if average > 6:
    print("Approved")
elif average > 4 and average < 6:
    print("Retake Exam")
else:
    print("Reproved")
