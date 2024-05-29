from collections import deque

n = int(input())

def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = 1
    while q:
        c = q.popleft()
        nc = arr[c]
        if not visit[nc]:
            q.append(nc)
            visit[nc] = 1

for i in range(n):
    m = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0,0)
    cnt = 0
    visit = [0] * (m+1)
    for j in range(1, m+1):
        if not visit[j]:
            bfs(j)
            cnt+=1
    print(cnt)