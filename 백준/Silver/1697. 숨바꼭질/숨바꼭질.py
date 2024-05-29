from collections import deque
def bfs():
    q = deque()
    q.append(s)
    while q:
        c = q.popleft()
        if c == t:
            print(visit[t])
            break
        for nc in (c+1, c-1, 2*c):
            if 0 <=  nc <= 10**5 and visit[nc] == 0:
                visit[nc]  = visit[c] + 1
                q.append(nc)

s,t  = map(int, input().split())
visit = [0] * (10**5 + 1)
bfs()