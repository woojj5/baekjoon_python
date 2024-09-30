from collections import deque

n, m , s = map(int, input().split())
arr = [[0] * (n+1) for i in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

visit = [0] * (n+1)
visit1 = [0] * (n+1)

def bfs(s):
    q = deque([s])
    visit[s] = 1
    while q:
        x = q.popleft()
        print(x, end = " ")
        for i in range(1, n+1):
            if visit[i] == 0 and arr[x][i] == 1:
                q.append(i)
                visit[i] = 1

def dfs(s):
    visit1[s]  = 1
    print(s, end = " ")
    for i in range(1, n+1):
        if visit1[i] == 0 and arr[s][i] == 1:
            dfs(i)


dfs(s)
print()
bfs(s)

