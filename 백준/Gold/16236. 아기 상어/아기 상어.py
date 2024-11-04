import copy
from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
size = 2
x,y, = 0,0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            x = i
            y = j

def bfs(x,y,ssize):
    q = deque()
    q.append((x,y))
    visit = [[0] * n for i in range(n)]
    distance = copy.deepcopy(visit)
    visit[x][y] = 1
    tmp = []
    while q:
        x,y = q.popleft()
        for i in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = x + i[0]
            ny = y + i[1]
            if 0<= nx < n and 0<= ny < n and visit[nx][ny] == 0 and arr[nx][ny] <= ssize:
                visit[nx][ny] = 1
                q.append((nx, ny))
                distance[nx][ny] = distance[x][y]+1
                if arr[nx][ny]< ssize and arr[nx][ny]!=0:
                    tmp.append((nx, ny, distance[nx][ny]))
    return sorted(tmp, key= lambda x: (-x[2], -x[0], -x[1]))
res = 0
cnt = 0
while 1:
    shark =  bfs(x,y,size)
    if len(shark) == 0:
        break
    nx,ny,dist = shark.pop()
    res+=dist
    arr[x][y], arr[nx][ny] = 0,0
    x,y = nx, ny
    cnt+=1
    if cnt == size:
        size+=1
        cnt = 0
print(res)

