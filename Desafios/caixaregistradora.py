import os

rounds = 1
produtos = []
i = 1
print("Lojas tabajara")

while True:
    while i != 0:
        print(f"Produto {rounds}:")
        p = int(input())
        rounds += 1
        produtos.append(p)
        if p == 0:
            i = i - 1

    total = sum(produtos)

    if p == 0:
        print(f"Total: {total}")
        print("Quantidade do pagamento: ")
        pag = int(input())
        troco = pag - total
        print(f"Troco: {troco}")
        break
