turmas = int(input("Escolha a quantidade de turmas: "))

alunos = []

for x in range(turmas):
    x = int(input("Quantidade de alunos: "))
    alunos.append(x)
    if x > 40:
        print("A turma deve ser menor que quarenta")
        alunos.remove(x)

m = len(alunos)
s = sum(alunos)

resultado = s / m


print(f"a média de alunos é {resultado}")
