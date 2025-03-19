from modulos.soma_notas import calcular_soma
from modulos.media_alunos import calcular_media

aluno = input("Digite o nome do aluno: ")
notas = float(input("Digite as notasdo aluno: "))
soma = calcular_soma(notas)
media = calcular_media(soma, len(notas))
print(f"A média das notas do aluno {aluno} é: {media:.2f}")
