from collections import deque
n,m,s = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]
visit = [0] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
def bfs(s):
    visit = [0] * (n+1)
    q = deque()
    q.append(s)
    visit[s] = 1
    while q:
        x = q.popleft()
        print(x, end = ' ')
        for i in range(1, n+1):
            if arr[x][i] and visit[i] == 0:
                visit[i] = 1
                q.append(i)
    print()

def dfs(s):
    visit[s] = 1
    print(s, end = " ")
    for i in range(1, n+1):
        if arr[s][i] and visit[i] == 0:
            visit[i] = 1
            dfs(i)
dfs(s)
print()
bfs(s)