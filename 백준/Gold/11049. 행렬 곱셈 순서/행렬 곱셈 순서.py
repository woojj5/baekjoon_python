n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for term in range(1, n):
    for i in range(n-term):
        j = i+term
        if term == 1:
            dp[i][j] = arr[i][0] * arr[j][0] * arr[j][1]
            continue
        dp[i][j] = 2**31
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i][0] * arr[k][1] * arr[j][1])
print(dp[0][n-1])
