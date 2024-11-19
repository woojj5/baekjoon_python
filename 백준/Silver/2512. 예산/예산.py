n = int(input())
lista = list(map(int, input().split()))
m = int(input())
s = 0; e = max(lista)
ans= 0
while s<= e:
    mid = (s+e)//2
    res = 0
    for i in range(len(lista)):
        if mid >= lista[i]:
            res+= lista[i]
        else:
            res+= mid

    if res <=m:
        s = mid+1
        ans = max(ans, mid)
    else:
        e = mid-1
print(ans)
