import heapq

n,m,k,s = map(int, input().split())
graph = [[] for i in range(n+1)]
inf = int(1e10)
distance = [inf] * (n+1)
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append((b, 1))
def bfs(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        cost, cur = heapq.heappop(q)
        for next, dist in graph[cur]:
            if cost + dist < distance[next]:
                distance[next] =  cost + dist
                heapq.heappush(q, (cost+ dist, next))

bfs(s)
ans = []
for i in range(len(distance)):
    if distance[i] == k:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)