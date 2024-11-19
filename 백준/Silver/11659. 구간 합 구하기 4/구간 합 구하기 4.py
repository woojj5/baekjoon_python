n,m = map(int, input().split())
lista= list(map(int, input().split()))
sum_lista = []
sum_lista.append(0)
total = 0
for i in range(n):
    total+= lista[i]
    sum_lista.append(total)
for i in range(m):
    a,b = map(int, input().split())
    print(sum_lista[b] - sum_lista[a-1])