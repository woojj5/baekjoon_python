import heapq
n = int(input())
arr = [[] for i in range(n+1)]
m = int(input())

for i in range(m):
    a,b,c  = map(int, input().split())
    arr[a].append([b,c])
s,e  = map(int, input().split())

def bfs(s):
    distances = [1e10] * (n+1)
    distances[s] = 0
    q = []
    heapq.heappush(q, (distances[s], s))
    while q:
        dist, node = heapq.heappop(q)
        if distances[node] < dist:
            continue
        for next_node, next_dist in arr[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(q, (distances[next_node], next_node))
    return distances[e]
print(bfs(s))