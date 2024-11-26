stringa = list(' '+input())
stringb = list(' '+input())
dp = [[0] * len(stringb) for i in range(len(stringa))]

for i in range(1, len(stringa)):
    for j in range(1, len(stringb)):
        if stringa[i] == stringb[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])