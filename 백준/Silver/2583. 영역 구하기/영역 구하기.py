from collections import deque
import copy
m,n,t = map(int, input().split())
graph = [[0] * m for i in range(n)]
visit = copy.deepcopy(graph)
for i in range(t):
    x1,y1, x2,y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            graph[j][k] = 1
cnt = []
count = 0
r_count = 0

def bfs(x,y):
    q  = deque()
    q.append((x,y))
    visit[x][y] = 1
    global r_count
    r_count = 1
    while q:
        x,y = q.popleft()
        for i in ((1,0), (-1, 0), (0, 1), (0, -1)):
            nx = x + i[0]
            ny = y + i[1]
            if 0<= nx < (n) and 0<= ny < (m) and graph[nx][ny] == 0 and visit[nx][ny] == 0:
                q.append((nx, ny))
                visit[nx][ny] = 1
                r_count+=1
    cnt.append(r_count)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visit[i][j] == 0:
            bfs(i, j)
print(len(cnt))
cnt.sort()
for i in cnt:
    print(i, end = " ")

