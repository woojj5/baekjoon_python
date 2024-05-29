n = 64
x = int(input())
arr = [0 for i in range(65)]
ind = 64
while True:
    if ind == x:
        arr[ind] = arr[ind] + 1
        print(arr[ind])
        break
    else:
        if ind > x:
            ind = ind//2
        elif ind < x:
            x = x - ind
            arr[x] = arr[x+ind] + 1