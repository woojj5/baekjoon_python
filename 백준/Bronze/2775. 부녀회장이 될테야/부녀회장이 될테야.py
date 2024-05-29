test_case= int(input())

for t in range(test_case):
    floor = int(input())
    num = int(input())
    arr = [[0 for i in range(15)]for _ in range(15)]
    for i in range(num+1):
        arr[0][i] = i
    
    for i in range(1, floor+1):
        for j in range(1, num+1):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    print(arr[floor][num])