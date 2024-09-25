n = int(input())
t_n = int(n//3) + 1
f_n = int(n//5) + 1
ans = 1e10
for i in range(0, f_n):
    for j in range(0, t_n):
        if 5*i + 3 * j == n:
            ans = min(ans, i+j)
if ans == 1e10:
    print(-1)
else:
    print(ans)