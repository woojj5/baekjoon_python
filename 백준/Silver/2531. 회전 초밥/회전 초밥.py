N, d, k, c = map(int, input().split())
lista = [int(input()) for i in range(N)]
sele = lista[:k]

res = 0
for i in range(N):
    sele.pop(0)
    sele.append(lista[(k+i)%N])
    res = max(res, len(set(sele + [c])))
    
    if res == d:
        break
print(res)
