n,m = map(int, input().split())

def dfs():
    if len(lista) == m:
        print(" ".join(map(str, lista)))
    for i in range(1, n+1):
        if i in lista:
            continue
        lista.append(i)
        dfs()
        lista.pop()

lista = []
dfs()