from collections import deque

m,n,h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visit = [[[0] * m for i in range(n)] for j in range(h)]
q = deque()


def bfs():
    while q:
        x,y,z = q.popleft()
        for i in ((1,0,0), (-1,0,0), (0, -1, 0), (0, 1, 0),  (0,0,1), (0,0,-1)):
            nx = x + i[0]
            ny = y + i[1]
            nz = z + i[2]
            if 0<= nx < h and 0<= ny <n and 0<= nz <m and matrix[nx][ny][nz] == 0 and visit[nx][ny][nz] == 0:
                q.append((nx, ny, nz))
                matrix[nx][ny][nz] = matrix[x][y][z] +1
                visit[nx][ny][nz] = 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1 and visit[i][j][k] == 0:
                q.append((i,j,k))
                visit[i][j][k] = 1

bfs()

res = -1000000
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0:
                print(-1)
                exit(0)
        res = max(res, max(matrix[i][j]))
print(res-1)
