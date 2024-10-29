import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost= dist+i[1]
            if cost< distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n,m = map(int, input().split())
s = int(input())
arr = [[]  for i in range(n+1)]
inf = 1e9
distance = [inf] * (n+1)
for months in range(m):
    v,e, w = map(int, input().split())
    arr[v].append((e,w))
dijkstra(s)
for i in range(1,n+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])
