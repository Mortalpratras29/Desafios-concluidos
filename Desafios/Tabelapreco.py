print("1- Loja de 1.99 2- Padaria")
esc = int(input())


if esc == 1:
    print("Lojas Quase Dois - Tabela de preços")
    for x in range(1, 51):
        p = x * 1.99
        print(f"{x}- R$ {p}")


elif esc == 2:
    print("Preço do pão: R$ 0.88")
    print("Panificadora Pão de Ontem - Tabela de preços")
    for x in range(1, 51):
        p = x * 0.18
        print(f"{x}- R$ {p}")

else:
    print("Escolha invalida")
