import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
t = int(input())
dict = [""] * 51
for i in range(n):
    dict[arr[i]] = str(i)
for i in range(1, t+1):
    if dict[i] == "":
        continue
    for j in range(n):
        if i + arr[j] > t:
            continue
        elif dict[i+arr[j]] == "":
            dict[i+arr[j]] = dict[i] + str(j)
            continue
        elif int(dict[i+arr[j]]) >= int(dict[i] + str(j)):
            continue
        dict[i+arr[j]] = dict[i] + str(j)
ans= 0
for i in range(t+1):
    if dict[i] == "":
        continue
    ans = max(ans, int(dict[i]))
print(ans)