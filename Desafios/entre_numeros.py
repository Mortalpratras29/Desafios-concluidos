n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))

soma_total = 0

for x in range(n1,n2):
    print(x, end= (" "))
    soma_total += x

print(f'Soma total: {soma_total} ')  
