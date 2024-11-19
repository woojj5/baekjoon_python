from collections import deque
m,n = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
ind = []
visit = [[0] * m for i in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i,j])
def bfs():
   while q:
       x,y = q.popleft()
       for dx,dy in [(0,1), (0,-1), (1,0), (-1,0)]:
           nx = x + dx
           ny = y + dy
           if 0<= nx < n and 0<= ny < m and  arr[nx][ny] == 0:
               arr[nx][ny] = arr[x][y] + 1
               q.append([nx, ny])
bfs()
res = 0
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)