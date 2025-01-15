import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for nxt_cost, nxt in graph[cur]:
            cst = nxt_cost + cost
            if dist[nxt] > cst:
                dist[nxt] = cst
                visit[nxt] = cur
                heapq.heappush(q, (cst, nxt))


n,m = map(int, input().split())
graph = [[] for i in range(n+1)]
dist = [INF] * (n+1)
visit = [0] * (n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

dijkstra(1)
print(n-1)
for i in range(2, n + 1):
    print(i, visit[i])







    