def union_parent(x,y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        arr[x] = y
    else:
        arr[y] = x

def find_parent(x):
    if arr[x] != x:
        arr[x] = find_parent(arr[x])
    return arr[x]

n,m = map(int, input().split())
arr = [i for i in range(n+1)]

for i in range(m):
    a,b,c = map(int, input().split())
    if a == 0:
        union_parent(b,c)
    else:
        if find_parent(b) == find_parent(c):
            print("YES")
        else:
            print("NO")

