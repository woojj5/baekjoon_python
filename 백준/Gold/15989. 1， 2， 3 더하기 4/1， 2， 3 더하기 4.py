iter = int(input())
arr = [1] * 100001
for i in range(2, 100001):
    arr[i] += arr[i-2]
for i in range(3, 100001):
    arr[i] += arr[i-3]
for _ in range(iter):
    n = int(input())
    print(arr[n])