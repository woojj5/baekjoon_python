import sys
input = sys.stdin.readline

V, E = map(int, input().split())
lista = [i for i in range(V + 1)]
rank = [0] * (V + 1)  # 유니온 바이 랭크를 위해 랭크 배열 생성
elist = []

for _ in range(E):
    elist.append(list(map(int, input().split())))
elist.sort(key=lambda x: x[2])

# 경로 압축을 적용한 find 함수
def find(x):
    if x != lista[x]:
        lista[x] = find(lista[x])  # 경로 압축
    return lista[x]

# 유니온 바이 랭크를 적용한 union 함수
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            lista[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            lista[rootX] = rootY
        else:
            lista[rootY] = rootX
            rank[rootX] += 1

ans = 0
for s, e, w in elist:
    if find(s) != find(e):
        union(s, e)
        ans += w

print(ans)
