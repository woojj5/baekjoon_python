from collections import deque
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

def bfs(x,y):
    q = deque([(x,y)])
    visit[x][y] =1
    while q:
        x,y = q.popleft()
        for dx, dy in ((1,0), (-1, 0), (0,1), (0,-1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if graph[nx][ny] !=0:
                    q.append((nx, ny))
                    visit[nx][ny] = 1
                else:
                    cnt[x][y] +=1
    return 1

year = 0
while True:
    answer = []
    visit = [[0] * m for _ in range(n)]
    cnt = [[0] * m for _ in range(n)]

    # 빙산과 접촉되어 있는 바닷물 확인
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visit[i][j]:
                answer.append(bfs(i, j))

    # 빙산을 깍아줌
    for i in range(n):
        for j in range(m):
            graph[i][j] -= cnt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if len(answer) == 0 or len(answer) >= 2:
        break
    year += 1

print(year) if len(answer) >= 2 else print(0)