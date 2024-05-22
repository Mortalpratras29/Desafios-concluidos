x = int(input("Selecione a quantidade de eleitores:  "))

Voto = 0

Canditado1 = 0
Canditado2 = 0
Canditado3 = 0

V = []

while Voto < x:
    V = input("Digite seu Voto(segredo):")
    Voto += 1


if V == 1:
    Canditado1 += 1
elif V == 2:
    Canditado2 += 1
else:
    Canditado3 += 1

if Canditado1 > Canditado2 and Canditado3:
    print("Candidato 1 venceu!")
elif Canditado2 > Canditado1 and Canditado3:
    print("Canditado 2 venceu!")
else:
    print("Canditado 3 venceu!")
