from collections import deque

n,k = map(int, input().split())
arr = deque(list(map(int, input().split())))
visit = deque([0] * len(arr))
ans = 0
while True:
    ans +=1
    arr.rotate(1)
    visit.rotate(1)

    visit[n-1] = 0
    for i in range(n-2, -1, -1):
        if visit[i] and not visit[i+1] and arr[i+1] >0:
            visit[i+1], visit[i] = 1, 0
            arr[i+1]-=1
    visit[n-1] = 0

    if arr[0] >0:
        visit[0] = 1
        arr[0]-=1
    
    if arr.count(0) >= k:
        break
    
print(ans)