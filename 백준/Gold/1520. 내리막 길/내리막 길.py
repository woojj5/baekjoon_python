import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
lista = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]


def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and lista[nx][ny] < lista[x][y]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]


print(dfs(0, 0))