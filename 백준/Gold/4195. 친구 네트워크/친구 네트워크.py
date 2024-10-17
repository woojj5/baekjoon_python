def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    else:
        parent[y] = x
        visit[x]+=visit[y]
    
def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

T = int(input())
for t in range(T):
    n = int(input())
    parent = dict()
    visit = dict()
    for j in range(n):
        
        a,b = map(str, input().split())

        if a not in parent:
            parent[a] = a
            visit[a] = 1

        if b not in parent:
            parent[b] = b
            visit[b] = 1
        
        union(a,b)
        print(visit[find(a)])