t = int(input())
for _ in range(t):
    dic  = dict()
    n = int(input())
    arr1 = list(map(int, input().split()))
    for i in arr1:
        dic[i] = 1
    m = int(input())
    arr2 = list(map(int, input().split()))
    for arr in arr2:
        if arr in dic:
            print(1)
        else:
            print(0)