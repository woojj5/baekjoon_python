import heapq
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
level = [0] * (n+1)
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    level[b]+=1

q = []

for i in range(1, n+1):
    if level[i] == 0:
        heapq.heappush(q, i)
ans = []
while q:
    x = heapq.heappop(q)
    ans.append(x)
    for node in graph[x]:
        level[node] -=1
        if level[node] == 0:
            heapq.heappush(q, node)
print(" ".join(map(str, ans)))