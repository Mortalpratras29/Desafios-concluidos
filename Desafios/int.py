lista = []
for x in range (1,6):
    numeros = int(input('Digite um numero: '))
    lista.append(numeros)

maximo = max(lista)

print('O numero mais alto dessa lista é: ', maximo)

soma = sum(lista)
media = soma /5

print(f'A soma entre os numeros é: {soma}')
print(f'A média entre os numeros é: {media}')




