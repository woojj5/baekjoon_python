n = int(input())
arr = [[1e10] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    arr[i][i] = 0

it = int(input())

for i in range(it):
    a,b,c = map(int, input().split())
    arr[a][b] = min(arr[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] = min(arr[i][j], arr[i][k]+ arr[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] == 1e10:
            print(0, end = " ")
        else:
            print(arr[i][j], end = " ")
    print()
