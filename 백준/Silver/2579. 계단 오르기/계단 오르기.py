n = int(input())
arr = [0] * (300)
for t in range(n):
    v = int(input())
    arr[t] = v

res = [0] * (300)
res[0] = arr[0]
res[1] = arr[0] + arr[1]
res[2] = max(arr[0], arr[1]) + arr[2]
for i in range(3, n):
    res[i] = max(res[i-3] + arr[i-1], res[i-2]) + arr[i]

print(res[n-1])