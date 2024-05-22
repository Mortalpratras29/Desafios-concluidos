while True:
    n1 = int(input("Digite Seu numero: "))

    def mortal(n1):
        mult = 1
        for x in range(1, n1):
            mult += x * mult
            print(mult)

    mortal(n1)

    Parar = int(input("Para encerrar digite 1, para continuar digite outro numero: "))
    if Parar == 1:
        print("Adeus")
        break
