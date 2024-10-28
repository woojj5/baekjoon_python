import sys
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    global ans, i
    x = find(x)
    y = find(y)
    if x == y:
        ans = i+1
    else:
        if x< y:
            parent[y] = x
        else:
            parent[x] = y

ans = 0
n,m = map(int, input().split())
parent = [i for i in range(n)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if not ans:
        union(x,y)
print(ans)