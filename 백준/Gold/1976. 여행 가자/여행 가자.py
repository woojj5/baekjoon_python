def union(x,y):
    x = find(x)
    y = find(y)
    if x> y:
        parent[x] = y
    else:
        parent[y] = x

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

n = int(input())
m = int(input())
parent = [i for i in range(n)]


for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j]:
            union(i,j)
plan = list(map(int, input().split()))
res = "YES"
for i in range(1, m):
    if parent[plan[i]-1] != parent[plan[0]-1]:
        res = "NO"
        break
print(res)