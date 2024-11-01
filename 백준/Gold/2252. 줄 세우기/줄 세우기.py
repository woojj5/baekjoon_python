from collections import deque
n, m = map(int, input().split())
arr = [[] for i in range(n+1)]
visit = [0] *(n+1)
for i in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    visit[b] +=1
q = deque()
for i in range(1, n+1):
    if visit[i] == 0:
        q.append(i)
ans = []
while q:
    tmp = q.popleft()
    ans.append(tmp)
    for i in arr[tmp]:
        visit[i] -=1
        if visit[i] == 0:
            q.append(i)
print(*ans)