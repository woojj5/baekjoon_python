from collections import defaultdict
def dfs(n):
    if dp[n]:
        return dp[n]
    dp[n] = dfs(n//q) + dfs(n//p)
    return dp[n]

n,p,q= map(int, input().split())
dp= defaultdict(int)
dp[0] = 1
print(dfs(n))