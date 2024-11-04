import heapq
n,m, X = map(int, input().split())
inf = int(1e10)
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

def bfs(x):
    q = []
    heapq.heappush(q, (0, x))
    visit = [inf] * (n+1)
    visit[x] = 0
    while q:
        dist, cur = heapq.heappop(q)
        if dist > visit[cur]:
            continue
        for node, distance in arr[cur]:
            new_dist = dist + distance
            if new_dist < visit[node]:
                visit[node]= new_dist
                heapq.heappush(q, (new_dist, node))
    return visit
res = 0
for i in range(1, n+1):
    go = bfs(i)
    back = bfs(X)
    res = max(res, go[X] + back[i])
print(res)