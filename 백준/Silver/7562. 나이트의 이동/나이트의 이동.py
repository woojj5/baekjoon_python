from collections import deque

dx = [+2, +1, -1, -2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]
t = int(input())

def bfs(a, b, c, d):
    q = deque()
    q.append((a, b))
    while q:
        curx, cury = q.popleft()
        if curx == c and cury == d:
            print(arr[curx][cury] - 1)
            break
        for i in range(8):
            nx = curx + dx[i]
            ny = cury + dy[i]
            if 0<= nx <= n-1 and 0<= ny <= n-1 and arr[nx][ny] == 0:
                arr[nx][ny] = arr[curx][cury] + 1
                q.append((nx, ny))

for time in range(t):
    n = int(input())
    arr = [[0] * n for i in range(n)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    arr[sx][sy] = 1
    bfs(sx, sy, ex, ey)
    #print(arr)
