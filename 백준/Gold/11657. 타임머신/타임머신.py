n,m = map(int, input().split())
inf = int(1e9)
graph = []
visit = [inf] * (n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph.append((a,b,c))

def bfs(start):
    visit[start] = 0
    for i in range(1, n+1):
        for j in range(m):
            cur = graph[j][0]
            next = graph[j][1]
            cost = graph[j][2]
            if cost + visit[cur] < visit[next] and visit[cur] != inf:
                visit[next] = visit[cur] + cost
                if i == n:
                    return True
    return False

chk = bfs(1)
if chk:
    print(-1)
else:
    for i in range(2, n+1):
        if visit[i] == inf:
            print(-1)
        else:
            print(visit[i])