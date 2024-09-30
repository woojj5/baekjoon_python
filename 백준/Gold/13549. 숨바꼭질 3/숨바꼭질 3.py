from collections import deque

def bfs(s, e):
    q = deque([s])
    visit[s] = 0
    while q:
        x = q.popleft()

        if x  == e:
            return visit[x]
        
        for i in (x*2, x-1, x+1):
            if 0<= i < limit and visit[i] == 0:
                if i == x * 2:
                    visit[i] = visit[x]
                    q.appendleft(i)
                else:
                    visit[i] = visit[x] + 1
                    q.append(i)

s, e = map(int, input().split())
limit = 100001
visit = [0] * limit
if s == 0:
    print(bfs(1, e) +1)
else:
    print(bfs(s,e))