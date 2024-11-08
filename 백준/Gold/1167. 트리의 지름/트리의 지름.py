from collections import deque
n = int(input())
graph = [[] for i in range(n+1)]

for i in range(n):
    lisa = list(map(int, input().split()))
    for i in range(1, len(lisa)//2):
        graph[lisa[0]].append((lisa[2*i-1], lisa[2*i]))

def bfs(x):
    q = deque([x])
    visit[x] = 1
    while q:
        x  = q.popleft()
        for e,w in graph[x]:
            if visit[e] == 0:
                q.append(e)
                visit[e] = 1
                distance[e] = distance[x] + w

distance = [0] * (n+1)
visit = [0] * (n+1)
bfs(1)

max_dist = max(distance)
max_node = distance.index(max_dist)

distance = [0] * (n+1)
visit = [0] * (n+1)
bfs(max_node)
print(max(distance))