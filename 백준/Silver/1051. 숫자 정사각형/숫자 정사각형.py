n,m = map(int, input().split())
ind = min(n,m)
arr = [list(map(int, input())) for _ in range(n)]
i,j = 0,0
ans = []
while ind > 0:
    if arr[i][j] == arr[i+ind-1][j+ind-1] == arr[i+ind-1][j] == arr[i][j+ind-1]:
        ans.append(ind**2)
        break
    
    j+=1
    if j+ind-1 >= m:
        i+=1
        j = 0
    
    if i + ind - 1 >= n:
        i = 0
        j = 0
        ind-=1

print(*ans)
