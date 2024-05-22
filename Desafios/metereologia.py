print("Menu meteriologico/ Digite 99 para sair")

i = 1
temps = []

while i != 99:
    print("Informe a temperatura(em celcius): ")
    t = int(input())
    temps.append(t)
    if t == 99:
        i = i + 98
        temps.remove(t)


mx = max(temps)
mn = min(temps)
q = len(temps)
s = sum(temps)

print(f"A menor temperatura registrada foi {mn}")
print(f"A maior temperatura registrada foi {mx}")
print(f"A temperatura média foi {s / q}")
