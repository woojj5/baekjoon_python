from collections import deque

def bfs(s1,s2):
    res = 1
    q = deque()
    q.append([s1,s2])
    visit[s1][s2] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < a and 0<= ny < a and visit[nx][ny] == 0 and arr[nx][ny] == 1:
                visit[nx][ny] = 1
                q.append([nx, ny])
                res = res + 1
    return res
a = int(input())
arr = []
visit = [[0] * a for i in range(a)]
for i in range(a):
    arr.append(list(map(int, input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
res_a = []
for i in range(a):
    for j in range(a):
        if arr[i][j] == 1 and visit[i][j] == 0:
            res_a.append(bfs(i,j))
res_a.sort()
print(len(res_a))
for i in res_a:
    print(i)
