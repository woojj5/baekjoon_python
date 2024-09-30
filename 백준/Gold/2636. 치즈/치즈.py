from collections import deque
def bfs():
    q = deque([(0,0)])
    melt = deque()
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<=ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if cheeze[nx][ny] == 0:
                    q.append([nx,ny])
                else:
                    melt.append([nx,ny])

    for x,y in melt:
        cheeze[x][y] = 0
    return len(melt)

n,m = map(int, input().split())
cheeze = []
cnt = 0
for i in range(n):
    cheeze.append(list(map(int, input().split())))
cnt+= sum(map(sum, cheeze))

dx = [1,-1,0,0]
dy = [0,0,-1,1]
time = 1

while True:
    visited = [[0] * m for i in range(n)]
    meltcnt = bfs()
    cnt -= meltcnt
    if cnt == 0:
        print(time, meltcnt, sep = "\n")
        break
    time+=1
