n = int(input())
arr = list(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))

arr.sort()

for element in arr2:
    l, h = 0, n-1
    check  = 0 
    while l<= h:
        m = (l+h)//2
        if arr[m] == element:
            check = 1
            print(1)
            break
        elif arr[m] > element:
            h  = m-1
            continue
        elif arr[m] < element:
            l = m+1
            continue
    if not check:
        print(0)
