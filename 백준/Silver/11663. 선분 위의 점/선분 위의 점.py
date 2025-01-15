import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
def find_start(arr, a):
    s,e = 0, n-1
    while s <= e:
        mid = (s+e)//2
        if int(arr[mid]) < a:
            s = mid + 1
        else:
            e = mid - 1
    return s
def find_max(arr, b):
    s,e = 0, n-1
    while s <= e:
        mid = (s+e)//2
        if int(arr[mid]) > b:
            e = mid - 1
        else:
            s = mid + 1
    return e

for _ in range(m):
    a,b = map(int, input().split())
    ma = find_start(arr, a)
    mb = find_max(arr, b)
    print(mb-ma+1)
