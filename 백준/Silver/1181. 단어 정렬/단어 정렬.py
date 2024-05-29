a = int(input())
arr = []
for i in range(a):
    b = input()
    arr.append(b)

arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key =len)
for i in arr:
    print(i)