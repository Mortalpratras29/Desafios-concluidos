n = int(input('Digite um numero: '))


def fibonacci(n):
    if n <= 0:
        return "N deve ser maior que zero"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_minus_2 = 0
        fib_minus_1 = 1
        for x in range (2, n):
            fib = fib_minus_1 + fib_minus_2
            fib_minus_2 = fib_minus_1
            fib_minus_1 = fib
        return fib

    
print("O", n, "º termo da sequência de Fibonacci é:", fibonacci(n))



