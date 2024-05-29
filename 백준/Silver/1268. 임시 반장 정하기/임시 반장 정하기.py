num = int(input())
arr = []
same = [0] * num
for i in range(num):
    a = list(map(int, input().split()))
    arr.append(a)
    same[i] = [0] * num


for i in range(5):
    for j in range(num):
        for k in range(j+1, num):
            if arr[j][i] == arr[k][i]:
                same[k][j] = same[j][k] = 1
cnt = [] 
for s in same:
    cnt.append(sum(s))
print(cnt.index(max(cnt)) + 1)