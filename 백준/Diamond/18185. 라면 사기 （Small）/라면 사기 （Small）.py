def one(x):
    global res
    res+= 3*arr[x]
def two(x):
    global res
    m = min(arr[x:x+2])
    arr[x]-=m
    arr[x+1]-=m
    res+=5*m
def thr(x):
    global res
    m = min(arr[x:x+3])
    arr[x]-=m
    arr[x+1]-=m
    arr[x+2]-=m
    res+=7*m

n= int(input())
arr = list(map(int, input().split())) + [0,0]
res = 0
for i in range(len(arr)-2):
    if arr[i+1]> arr[i+2]:
        m = min(arr[i], arr[i+1]-arr[i+2])
        arr[i]-=m
        arr[i+1]-=m
        res+=5*m
        thr(i)
        one(i)
    else:
        thr(i)
        two(i)
        one(i)
print(res)
