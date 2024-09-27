n,k = map(int, input().split())
lista = [int(input()) for i in range(n)]
s = 1
e = max(lista)
while s<= e:
    m = (s+e)//2
    line = 0
    for i in lista:
        line+= i//m
    if line >= k:
        s = m+1
    else:
        e = m-1
print(e)
