n = int(input())
arr = list(map(int, input().split()))
dp = [1] * (n)

dp2 = [1] * (n)
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j]+1, dp[i])

for i in range(n-2, -1, -1):
    for j in range(i, n):
        if arr[j] < arr[i]:
            dp2[i] = max(dp2[j]+1, dp2[i])

#일단 이렇게 만들면 정순과 역습을 구함

#문제는 바이토닉 수열의 경우 정순 + 역순의 합을 구해야 해서 이걸 다르게 봐야하겠네

res = []
for i in range(n):
    res.append(dp[i] + dp2[i]-1)
print(max(res))