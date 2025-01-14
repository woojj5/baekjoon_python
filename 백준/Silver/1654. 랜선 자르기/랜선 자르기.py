n,m = map(int, input().split())
arr = [int(input()) for i in range(n)]
s,e = 1, max(arr)

while s<=e:
    res = 0
    mid = int((s+e)/2)
    for i in range(n):
        res+=int(arr[i]//mid)
    if res >= m:
        s = mid+1
    else:
        e = mid-1
print(e)