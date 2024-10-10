n,m = map(int, input().split())
block = [*map(int, input().split())]
res = 0
for i in range(1, m-1):
    left = max(block[:i])
    right = max(block[i+1:])

    lower_one = min(left, right)

    if block[i] < lower_one:
        res+= (lower_one - block[i])
print(res)