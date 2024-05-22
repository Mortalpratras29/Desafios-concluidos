while True:
    Pais_a = int(input("Digite a população 1 : "))
    P1 = float(input("Digite a taxa de crescimento 1 : "))
    Pais_b = int(input("Digite a população 2: "))
    P2 = float(input("Digite a taxa de crescimento 2 : "))

    P1 = P1 / 100 + 1
    P2 = P2 / 100 + 1

    anus = 0

    while Pais_a != Pais_b:
        Pais_a = Pais_a * P1
        Pais_b = Pais_b * P2
        anus += 1

        print(f"Pais ultrapassado em : {anus} ")

    repetir = str(input("Repeteco? (S/N): "))
    if repetir.upper() != "S":
        print("Adeus")
        break
