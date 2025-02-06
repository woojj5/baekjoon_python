n = 19
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0,1,-1,1]
dy = [1,1,1,0]
chk1 = 0
res = 0
def dfs(x,y):
    global res
    for i in range(4):
        cnt = 1
        nx,ny = x+dx[i], y+dy[i]
        while 0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y]:
            cnt+=1
            nx+=dx[i]
            ny+=dy[i]
            if cnt == 5:
                if not(0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y]):
                    if not(0<=x-dx[i] < n and 0<=y-dy[i] < n and graph[x-dx[i]][y-dy[i]] == graph[x][y]):
                        print(graph[x][y])
                        print(x+1,y+1)
                        exit(0)
                    else: break
                else: break
                    
            
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            dfs(i,j)
print(0)