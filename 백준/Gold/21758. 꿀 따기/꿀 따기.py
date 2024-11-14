n = int(input())
lista= list(map(int, input().split()))
res = [lista[0]]+[0] * (n-1)
con = 0
for i in range(1, n):
    res[i] = res[i-1] + lista[i]

for i in range(1, n-1):
    right = 2 * res[-1]  - lista[0] - lista[i] - res[i]
    left =  res[-1] - lista[-1] - lista[i] + res[i-1]
    mid =  res[i] - lista[0] + res[-1] - res[i-1] - lista[-1]
    con = max(con, right, left, mid)
print(con)
