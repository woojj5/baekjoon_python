n = int(input())
for i in range(n//2, n):
    tmp = i
    res = i
    while i != 0:
        res += (i%10)
        i//=10
    if res == n:
        print(tmp)
        exit()
print(0)
