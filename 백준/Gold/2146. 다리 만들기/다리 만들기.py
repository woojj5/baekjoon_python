from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
inf = int(1e10)
visit = [[0] * n for i in range(n)]
num = 1
res= 0
def bfs(i,j):
    q = deque()
    q.append([i,j])
    while q:
        x,y = q.popleft()
        for dx,dy in ([1,0], [-1,0], [0,1], [0,-1]):
            nx,ny = x+dx, y+dy
            if 0<= nx < n and 0<= ny< n and not visit[nx][ny] and graph[nx][ny]:
                visit[nx][ny] = 1
                graph[nx][ny] = num
                q.append([nx, ny])
def bfs1(v):
    q = deque()
    dist = [[-1] *n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == v:
                dist[i][j] = 0
                q.append([i,j])
    while q:
        x,y = q.popleft()
        for dx,dy in ([1,0], [-1,0], [0,1], [0,-1]):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] and graph[nx][ny] != v:
                    return dist[x][y]
                elif graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])
    return int(1e9)

for i in range(n):
  for j in range(n):
    if graph[i][j] and not visit[i][j]:
      visit[i][j] = 1
      graph[i][j] = num
      bfs(i,j)
      num += 1
res= inf
# 최단거리 구하기
for v in range(1,num):
  res = min(res, bfs1(v))
print(res)
