def cal(x,y,z, arr):
    tmp  = 10000 
    for i in range(x+1):
        for j in range(y+1):
            arr[i][j] = 3*(i)+  5*(j)
    
    for i in range(x+1):
        for j in range(y+1):
            if tmp > (i+j) and arr[i][j] == z:
                tmp = i+j
    if tmp == 10000 or tmp == 0: tmp = -1
    return tmp

a = int(input())
x = a //3
y = a // 5

arr = [[0 for i in range(y+1)]for _ in range(x+1)]

print(cal(x,y,a, arr))
