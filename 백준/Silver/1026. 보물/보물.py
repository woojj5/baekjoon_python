n = int(input())
ar = list(map(int, input().split()))
ar1 = list(map(int, input().split()))

ar.sort()
ar1.sort(reverse=True)

res = 0
for i in range(len(ar)):
    res+= (ar[i] * ar1[i])

print(res)
