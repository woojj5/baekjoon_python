n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = max(arr)
e = sum(arr)
while s<=e:
    mid = (s+e)//2
    tot = 0
    cnt = 1
    for i in arr:
        if i + tot > mid:
            tot = 0
            cnt+=1
        tot+=i
    if cnt <= m:
        ans = mid
        e = mid-1
    else:
        s =  mid+1
print(ans)  