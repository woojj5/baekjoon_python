from collections import deque
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]

def bfs(i,j):
    cnt = 1
    q = deque()
    q.append([i,j])
    visit[i][j] = 1
    while q:
        x,y = q.popleft()
        for nx, ny in [(x+1, y), (x-1, y), (x,y+1),(x, y-1)]:
            if 0<=nx<n and 0<=ny<n and arr[nx][ny ]and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append([nx, ny])
                cnt+=1
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] and not visit[i][j]:
            result.append(bfs(i,j))
print(len(result))
result.sort()
for r in result:
    print(r)