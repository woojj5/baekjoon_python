from collections import deque
def bfs():
    q = deque()
    q.append((0,0,0))
    while q:
        x,y,c = q.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][c]
        for i in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nx = x + i[0]
            ny = y + i[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 1 and c == 0:
                visit[nx][ny][1] = visit[x][y][0] + 1
                q.append((nx, ny, 1))
            elif arr[nx][ny] == 0 and visit[nx][ny][c] == 0:
                visit[nx][ny][c] = visit[x][y][c] + 1
                q.append((nx, ny, c))
    return -1
n, m = map(int, input().split())
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1
arr = [list(map(int, input())) for i in range(n)]
print(bfs())