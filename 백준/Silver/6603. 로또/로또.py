from itertools import combinations

while True:
    lista = list(map(int, input().split()))
    a = lista.pop(0)
    if a == 0:
        break
    for combo in combinations(lista, 6):
        print(" ".join(map(str, combo)))
    print()