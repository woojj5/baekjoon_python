from collections import deque
area = []
def bfs(x,y):
    cnt  = 1
    q = deque([(x,y)])
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in ((1,0), (-1, 0), (0, 1), (0,-1)):
            nx= x+dx
            ny= y+dy
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0 and graph[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = 1
                cnt+=1
    area.append(cnt)



n,m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
visit = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visit[i][j]:
            bfs(i,j)
if len(area):
    print(len(area))
    print(max(area))
else:
    print(0)
    print(0)

