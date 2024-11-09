from collections import deque
n,m = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input())))
dist = [[-1] *n for i in range(m)]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    dist[x][y] = 0
    while q:
        x,y = q.popleft()
        for dx,dy in ((1,0), (-1, 0), (0,1), (0,-1)):
            nx = x + dx
            ny = y + dy
            if 0<= nx < m and 0<= ny < n and dist[nx][ny] == -1:
                if graph[nx][ny] == 0: q.appendleft([nx, ny])
                else: q.append([nx, ny])
                dist[nx][ny] = dist[x][y] + graph[nx][ny]
bfs(0,0)
print(dist[m-1][n-1])
