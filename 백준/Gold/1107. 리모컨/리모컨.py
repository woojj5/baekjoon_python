n = int(input())
m = int(input())
if m == 0:
    disabled = []
else:
    disabled = list(map(int, input().split()))
min_count = abs(100 - n)
for i in range(999999):
    num = str(i)
    for nin in num:
        if int(nin) in disabled:
            break
    else:
        min_count = min(min_count, abs(n-i)+ len(num))
print(min_count)