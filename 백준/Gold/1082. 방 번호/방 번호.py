import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
t = int(input())
dict = [""]*(51)
for i in range(n):
    dict[arr[i]] = str(i)
for i in range(t+1):
    for j in range(n):
        if arr[j] + i <= t:
            if dict[i+arr[j]]  == "": dict[i+arr[j]] = dict[i] + str(j)
            elif int(dict[i+arr[j]]) < int(dict[i] + str(j)): dict[i+arr[j]] = dict[i] + str(j)
ans = 0
for i in range(1, t+1):
    if dict[i] == "":
        continue
    ans = max(ans, int(dict[i]))
print(ans)