from collections import deque
s,e = map(int, input().split())
q = deque()
q.append(s)
visit = [-1] * int(1e5+1)
visit[s] = 0
cnt = 0
while q:
    x = q.popleft()
    if x == e:
        cnt+=1
    for nx in (x-1, x+1, 2*x):
        if 0<= nx<= 1e5 and (visit[nx] == -1 or visit[nx] >= visit[x]+1):
            visit[nx] = visit[x] + 1
            q.append(nx)

print(visit[e])
print(cnt)