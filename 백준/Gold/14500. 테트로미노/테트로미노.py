from collections import deque

n,m = map(int, input().split())
lista = [list(map(int, input().split())) for i in range(n)]
visited = [[0] * m for i in range(n)]
dx = [0,0,1,-1]
dy = [-1,1,0,0]
maxm = 0

def dfs(x,y, tmp, cnt):
    global maxm
    if cnt == 4:
        maxm = max(maxm, tmp)
        return max
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=  nx  < n and 0<= ny < m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, tmp + lista[nx][ny], cnt+1)
            visited[nx][ny] = 0

def bfs2(x,y):
    global maxm
    for i in range(4):
        tmp = lista[x][y]
        for j in range(3):
            t = (i+j) % 4
            nx = x + dx[t]
            ny = y + dy[t]

            if 0<= nx < n and 0<= ny < m:
                tmp += lista[nx][ny]
        maxm = max(maxm, tmp)

for i in range(n):
    for j in range(m):
        # 시작점 visited 표시
        visited[i][j] = 1
        dfs(i, j, lista[i][j], 1)
        visited[i][j] = 0

        bfs2(i, j)

print(maxm)



