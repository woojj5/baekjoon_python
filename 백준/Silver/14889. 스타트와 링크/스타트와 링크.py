n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [0] * n
INF = 2147000000
res = INF

def dfs(L, idx):
    global res
    if L == n//2:
        A = 0
        B = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    A+= board[i][j]
                elif not visited[i] and not visited[j]:
                    B+= board[i][j]
        res = min(res, abs(A-B))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            dfs(L+1, i)
            visited[i]  = 0

dfs(0,0)
print(res)