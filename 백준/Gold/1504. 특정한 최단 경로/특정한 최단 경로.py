import sys
from heapq import heappop, heappush
input = sys.stdin.readline

inf = int(1e10)
n,m = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    u,v,w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

s1, s2 = map(int, input().split())

def dijstra(s, e):
    dis = [inf] *(n+1)
    dis[s] = 0
    q = [[0, s]]
    while q:
        a,b  = heappop(q)
        if a > dis[b]: continue
        for w,v in graph[b]:
            if dis[v] > dis[b] + w:
                dis[v] = dis[b] + w
                heappush(q, [dis[v], v])
    return dis[e]

p1 = dijstra(1, s1) + dijstra(s1, s2) + dijstra(s2, n)
p2 = dijstra(1, s2) + dijstra(s2, s1) + dijstra(s1, n)

if p1 >= inf and p2 >= inf:
    print(-1)
else:
    print(min(p1, p2))