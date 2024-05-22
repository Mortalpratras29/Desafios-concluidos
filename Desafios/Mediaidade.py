# Esse progama lista 5 idades e fala se as idades estão entre esses parametros

c = 0
while c <= 5:
    n = int(input("Digite sua idade: "))
    c += 1

if n > 0 and n <= 25:
    print("As idades estão entre 0 e 25 anos")
elif n > 25 and n <= 60:
    print("As idades estão entre 26 e 60 anos")
else:
    print("Idades maiores que 60 anos")
