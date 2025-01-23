from collections import deque
k = int(input())
def bfs(x,color):
    q = deque()
    q.append(x)
    visit[x] = color
    while q:
        x = q.popleft()
        for next in graph[x]:
            if not visit[next]:
                visit[next] = -visit[x]
                q.append(next)
            elif visit[next] == visit[x]:
                return True
    return False



for _ in range(k):
    n,m = map(int, input().split())
    visit = [0] * (n+1)
    graph = [[]  for _ in range(n+1)]
    cnt = 0
    for i in range(m):
        x,y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    for i in range(1, n+1):
        if not visit[i]:
            if bfs(i, 1):
                print("NO")
                break
    else:
        print("YES")

