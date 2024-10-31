from collections import deque
import copy
def bfs(x,y, arr, v):
    q = deque()
    q.append((x,y))
    v[x][y]  = 1
    while q:
        x,y = q.popleft()
        for k in ((-1,0), (1,0), (0, 1), (0, -1)):
            #print(i)
            nx = x + k[0]
            ny = y + k[1]
            if 0<= nx < n and 0<= ny < n and v[nx][ny] == 0 and arr[nx][ny] == arr[x][y]:
                v[nx][ny] = 1
                q.append((nx, ny))

n = int(input())
pic = [list(input()) for i in range(n)]
pic2  = copy.deepcopy(pic)
visit = [[0] * n for i in range(n)]
visit2 = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if pic2[i][j] == "G":
            pic2[i][j] = "R"
res = 0
res2 = 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i,j, pic, visit)
            res+=1

for i in range(n):
    for j in range(n):
        if visit2[i][j] == 0:
            bfs(i,j, pic2, visit2)
            res2+=1
print(res, res2)