import os

array = []

x = None

while True:

    print(
        """𓂀ℂ𝕒𝕦𝕔𝕦𝕝𝕒𝕕𝕠𝕣𝕒𓂀

    Para adição digite 1
    Para subtração digite 2
    Para multiplicação digite 3
    Para Divisão digite 4
    Para Raiz digite 5
    Ver Histórico 6
    Para sair digite 7
        """
    )

    def selct():
        y = int(input("Escolha o segundo numero numero: "))
        return y

    def adicao(x, y):
        soma = x + y
        return soma

    def raiz_quadrada(numero):
        if numero < 0:
            raise ValueError(
                "Não é possível calcular a raiz quadrada de um número negativo."
            )
        if numero == 0:
            return 0
        approx = numero / 2.0
        while True:
            raiz_quadrada = (approx + numero / approx) / 2.0
            if abs(raiz_quadrada - approx) < 0.0001:
                return raiz_quadrada
            approx = raiz_quadrada

    def subtracao(x, y):
        sub = x - y
        return sub

    def multiplicacao(x, y):
        mult = x * y
        return mult

    def divisao(x, y):
        div = x / y
        if x == 0 or y == 0:
            print("Impossivel dividir por 0")
        return div

    escolha = int(input())

    if escolha == 1:
        if x is None:
            x = int(input("Escolha o primeiro numero: "))
        y = selct()
        resultado = adicao(x, y)
        msg = f"A soma entre {x} e {y} é igual a {resultado}"
        array.append(resultado)
        print(msg)
        x = resultado
    elif escolha == 2:
        if x is None:
            print("Você precisa realizar uma adição antes de uma subtração.")
            continue
        y = selct()
        resultado = subtracao(x, y)
        msg = f"A subtração entre {x} e {y} é igual a {resultado}"
        array.append(resultado)
        print(msg)
        x = resultado
    elif escolha == 3:
        if x is None:
            print("Você precisa realizar uma adição antes de uma multiplicação.")
            continue
        y = selct()
        resultado = multiplicacao(x, y)
        msg = f"A multiplicação entre {x} e {y} é igual a {resultado}"
        array.append(resultado)
        print(msg)
        x = resultado
    elif escolha == 4:
        if x is None:
            print("Você precisa realizar uma adição antes de uma divisão.")
            continue
        y = selct()
        resultado = divisao(x, y)
        msg = f"A divisão entre {x} e {y} é igual a {resultado}"
        array.append(resultado)
        x = resultado
    elif escolha == 5:
        if x is None:
            print("Você precisa realizar uma adição antes de calcular a raiz.")
            continue
        resultado = raiz_quadrada(x)
        msg = f"A raiz quadrada de {x} é igual a {resultado}"
        array.append(resultado)
        print(msg)
    elif escolha == 6:
        print("Histórico de operações:")
        print(array)
    elif escolha == 7:
        print("Saindo")
        os.system("cls")
        break
    else:
        print("Escolha inválida")
