a = int(input())
arr = [[ 0 for i in range(2)] for _ in range(40+1)]

arr[0] = [1,0]
arr[1] = [0,1]
for i in range(2, 40+1):
    arr[i][0] = arr[i-2][0] + arr[i-1][0]
    arr[i][1] = arr[i-2][1] + arr[i-1][1]

for i in range(a):
    b = int(input())
    print(arr[b][0], end = " ")
    print(arr[b][1] , end = " ")