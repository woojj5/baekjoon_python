n = int(input())
arr = list(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))
dict1 = {}
for i in arr:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] =  1

for i in arr2:
    if i in dict1:
        print(dict1[i], end = " ")
    else:
        print(0 , end = " ")