n,k = map(int, input().split())
lista = list(map(int, input().split()))
lista.sort()
s = 1
e = max(lista)
while s<= e:
    m = (s+e)//2
    res = 0
    for i in lista:
        if i >= m:
            res+= (i-m)
    if res >= k:
        s = m+1
    else:
        e = m-1
print(e)

    