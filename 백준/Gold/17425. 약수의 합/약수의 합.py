import sys
input = sys.stdin.readline
t = int(input())
Max = 1000000
dp = [1] * (Max+1)
arr = [0] * (Max+1)
for i in range(2, Max+1):
    j = 1
    while i*j <= Max:
        dp[i*j]+=i
        j+=1
for i in range(1, Max+1):
    arr[i] = arr[i-1] + dp[i]
for i in range(t):
    n = int(input())
    print(arr[n])