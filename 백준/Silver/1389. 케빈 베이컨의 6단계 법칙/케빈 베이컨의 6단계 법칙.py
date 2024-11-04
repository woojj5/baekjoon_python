import sys
input = sys.stdin.readline
inf = int(1e10)
n,m = map(int, input().split())
graph  = [[inf] * (n+1) for i in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

bacon = inf
answer = 0
for i in range(n, 0, -1):
    s = sum(graph[i][1:])
    if bacon >= s:
        bacon = s
        answer = i
print(answer)