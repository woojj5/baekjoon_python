board = [list(map(int, input().split())) for _ in range(19)]
res = 0
n = 19
dx = [0,1,-1,1]
dy = [1,1,1,0]

def dfs(x,y):
    global res
    for i in range(4):
        cnt = 1
        nx = x + dx[i]
        ny = y + dy[i]
        while 0<=nx < n and 0<= ny < n and board[nx][ny] == board[x][y]:
            nx+=dx[i]
            ny+=dy[i]
            cnt+=1
            if cnt == 5:
                if not(0<=nx < n and 0<= ny < n and board[nx][ny] == board[x][y]):
                    if not(0<=x-dx[i] < n and 0<= y-dy[i] < n and board[x][y] == board[x-dx[i]][y-dy[i]]):
                        print(board[x][y])
                        print(x+1, y+1)
                        exit(0)
                    else:break
                else:break
             
for i in range(n):
    for j in range(n):
        if board[i][j]:
            dfs(i,j)
print(0)