n1 = int(input("Digite seu range: "))
lista = []
for x in range(1, n1 + 1):
    lista.append(x)

maximo = max(lista)
minimo = min(lista)

print("O numero mais alto dessa lista é: ", maximo)
print("O numero mais baixo dessa lista é: ", minimo)

soma = sum(lista)
media = soma / n1

print(f"A soma entre os numeros é: {soma}")
print(f"A média entre os numeros é: {media}")
