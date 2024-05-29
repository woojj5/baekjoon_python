iter = int(input())
arr = [[0 for _ in range(3)] for i in range(iter)]
choice = [[0 for _ in range(3)] for i in range(iter)]
for i in range(iter):
    length = list(map(int, input().split()))
    for j in range(len(length)):
        arr[i][j] = length[j]
choice[0][0] = arr[0][0]
choice[0][1] = arr[0][1]
choice[0][2] = arr[0][2]


for i in range(1, iter):
    choice[i][0] = min(choice[i-1][1],choice[i-1][2]) +  arr[i][0]
    choice[i][2] = min(choice[i-1][1],choice[i-1][0]) +  arr[i][2]
    choice[i][1] = min(choice[i-1][0],choice[i-1][2]) +  arr[i][1]

print(min(choice[iter-1]))