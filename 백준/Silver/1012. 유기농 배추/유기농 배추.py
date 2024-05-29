from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    visit[x][y] = 1
    q = deque()
    q.append((x,y))
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<= ny <m and visit[nx][ny] == 0 and arr[nx][ny] == 1:
                visit[nx][ny] = 1
                q.append((nx,ny))

time = int(input())
for t in range(time):
    n,m,s = map(int, input().split())
    arr = [[0 for i in range(m)] for j in range(n)]
    visit = [[0 for i in range(m)] for j in range(n)]
    for i in range(s):
        a, b = map(int, input().split())
        arr[a][b] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visit[i][j] == 0:
                dfs(i,j)
                cnt+=1
    print(cnt)
    