def one(x):
    global res
    res+= (val[1] + 0*val[2])*arr[x]
def two(x):
    global res
    m = min(arr[x:x+2])
    arr[x]-=m
    arr[x+1]-=m
    res+=(val[1] + 1*val[2])*m
def thr(x):
    global res
    m = min(arr[x:x+3])
    arr[x]-=m
    arr[x+1]-=m
    arr[x+2]-=m
    res+=(val[1] + 2*val[2])*m

val = list(map(int, input().split()))
arr = list(map(int, input().split())) + [0,0]
res = 0
if val[1] <= val[2]:
    res+=sum(arr)*val[1]
else:
    for i in range(len(arr)-2):
        if arr[i+1]> arr[i+2]:
            m = min(arr[i], arr[i+1]-arr[i+2])
            arr[i]-=m
            arr[i+1]-=m
            res+=(val[1] + 1*val[2])*m
            thr(i)
            one(i)
        else:
            thr(i)
            two(i)
            one(i)
print(res)
