n = int(input())
lista = list(map(int, input().split()))
res = int(input())
if sum(lista) <= res:
    print(max(lista))
    exit()
start = 0; end = res; ans = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for ele in lista:
        tmp += ele if ele <= mid else mid
    if tmp <= res:
        ans = max(ans, mid)
        start = mid+1
    else:
        end = mid-1
print(ans)