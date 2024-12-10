from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    result = [0 for i in range(m+1)]
    visit = [[0 for i in range(m)] for j in range(n)]
    def bfs(x,y):
        q = deque()
        q.append([x,y])
        cnt = 0
        visit[x][y] = 1
        min_y, max_y = y,y
        while q:
            x,y = q.popleft()
            min_y = min(y, min_y)
            max_y = max(y, max_y)
            cnt+=1
            for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx = x + dx
                ny = y + dy
                if 0<= nx < len(land) and 0<= ny < len(land[0]) and land[nx][ny] == 1 and visit[nx][ny] == 0:
                    q.append([nx, ny])
                    visit[nx][ny] = 1
        for i in range(min_y, max_y+1):
            result[i]+= cnt
    answer = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] and not visit[i][j]:
                bfs(i,j)
    answer = max(result)
    return answer