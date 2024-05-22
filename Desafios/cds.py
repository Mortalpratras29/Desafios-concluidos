cds = int(input("Quantidade de cds: "))

precos = []

for x in range(cds):
    x = float(input("Preço de cada cd: "))
    precos.append(x)


media = sum(precos) / cds

print(f"A media de preços do seus cds é {media}")
