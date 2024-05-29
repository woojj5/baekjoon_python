from collections import deque

def floot(x,y, h):
    q = deque()
    q.append([x,y])
    visit[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n and visit[nx][ny] == 0 and arr[nx][ny] > h:
                visit[nx][ny] = 1
                q.append([nx,ny])
n = int(input())
arr = []
lar = 0
lea = 101
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    ar = list(map(int, input().split()))
    arr.append(ar)
    lar = max(lar, max(ar))
    lea = min(lea, min(ar))

cnt = 0
for t in range(lar):
    tmp = 0
    visit = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= t:
                visit[i][j] = -1
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                floot(i,j, t)
                tmp+=1
    cnt = max(cnt, tmp)
print(cnt)