n,m = map(int, input().split())
arr = [i for i in range(n+1)]
visit =  [0] * (n+1)
elist = []
for i in range(m):
    elist.append(list(map(int, input().split())))
elist.sort(key= lambda  x: x[2])

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    return arr[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x< y:
        arr[x] = y
    else:
        arr[y] = x

ans = 0
for v,e,w in elist:
    if find(v) != find(e):
        union(v,e)
        ans+=w
print(ans)
