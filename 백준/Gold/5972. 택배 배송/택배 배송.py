import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
INF = float("inf") # 무한대 상수 선언

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)   

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
def dijikstra(s):
    q = []
    distance[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for next in graph[cur]:
            cost = dist + next[1]

            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

    return distance[n]

print(dijikstra(1))