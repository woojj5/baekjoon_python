x,y = map(int, input().split())
arr = []
for i in range(x):
    x_arr = input()
    arr.append(x_arr)
visit = [[0] * y for j in range(x)]
rcnt = ccnt = 0
for i in range(x):
    if "X" not in arr[i]:
        rcnt +=1
for j in range(y):
    if "X" not in [arr[i][j] for i in range(x)]:
        ccnt +=1

print(max(ccnt, rcnt))