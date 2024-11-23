import copy
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
if n <= 2:
    print(sum(arr))
else:
    res = copy.deepcopy(arr)
    res[1] = arr[0] + arr[1]
    res[2] = max(arr[0], arr[1]) + arr[2]
    for i in range(3,n):
        res[i] = max(res[i-3] + arr[i-1], res[i-2]) + arr[i]
    print(res[n-1])