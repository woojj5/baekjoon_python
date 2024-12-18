from collections import deque
def solution(land):
    n = len(land)
    m = len(land[0])
    res = [0 for i in range(m+1)]
    arr = [[0 for i in range(m)] for j in range(n)]
    def bfs(x,y):
        q =deque()
        q.append([x,y])
        arr[x][y] = 1
        min_y, max_y = y,y
        cnt = 0
        while q:
            x,y = q.popleft()
            min_y = min(y, min_y)
            max_y = max(y, max_y)
            cnt+=1
            for dx,dy in [[1,0], [-1,0], [0,1], [0,-1]]:
                nx = x + dx
                ny = y + dy
                if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0 and land[nx][ny]:
                    arr[nx][ny] = 1
                    q.append([nx, ny])      
    
        for i in range(min_y, max_y+1):
            res[i]+=cnt
    answer = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 and land[i][j]:
                bfs(i,j)
    answer = max(res)
    return answer