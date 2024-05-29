from collections import deque
import sys
input = sys.stdin.readline

knight_x = [2,2,-2,-2,1,1,-1,-1]
kngiht_y = [1,-1,1,-1,2,-2,2,-2]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(t):
    q = deque()
    q.append((0,0,t))
    visit = [[[0] * (t + 1) for _ in range(n)] for _ in range(m)]
    while q:
        x,y,k = q.popleft()
        if x == m-1 and y == n-1:
            return visit[x][y][k]
        
        if k > 0:
            for i in range(8):
                nx = x + knight_x[i]
                ny = y + kngiht_y[i]
                if 0<= nx <=m-1 and 0<=ny <= n-1 and arr[nx][ny] != 1 and visit[nx][ny][k-1] == 0:
                    visit[nx][ny][k-1] = visit[x][y][k] + 1
                    q.append((nx,ny,k-1))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <=m-1 and 0<=ny <= n-1 and arr[nx][ny] != 1 and visit[nx][ny][k] == 0 :
                visit[nx][ny][k] = visit[x][y][k] + 1
                q.append((nx,ny,k))
    return -1

t = int(input())
n,m = map(int, input().split())
arr = []
#print(visit[0])
for i in range(m):
    arr.append(list(map(int, input().split())))
result = bfs(t)
print(result)