time = int(input())
arr = [list(map(int, input().split())) for i in range(time)]
arr.sort(key= lambda x: (x[1], x[0]))
e=ans=0
for x,y in arr:
    if e <= x:
        ans+=1
        e = y
print(ans)