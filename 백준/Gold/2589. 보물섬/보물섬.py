from collections import deque
n,m = map(int, input().split())
graph = [list(input()) for i in range(n)]
def bfs(x,y):
    q = deque()
    q.append([x,y])
    visit = [[0] * m for i in range(n)]
    visit[x][y] = 1
    cnt = 0
    while q:
        x,y = q.popleft()
        for dx,dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx = x + dx
            ny = y + dy
            if 0<= nx< n and 0<= ny < m and visit[nx][ny] == 0 and graph[nx][ny] == 'L':
                visit[nx][ny] = visit[x][y] + 1
                cnt = max(cnt, visit[nx][ny])
                q.append((nx, ny))
    return cnt-1
res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            res = max(res, bfs(i,j))
print(res)