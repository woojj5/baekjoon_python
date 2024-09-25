def check(data):
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if data[i][j] == data[i][j-1]:
                cnt+=1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
        cnt=1
        for j in range(1 , n):
            if data[j][i] == data[j-1][i]:
                cnt+=1
            else:
                cnt = 1    
            max_cnt = max(cnt, max_cnt)
    return max_cnt

n = int(input())
arr = [list(input()) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if j+1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            cnt = check(arr)
            ans = max(cnt, ans)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if i+1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            cnt = check(arr)
            ans = max(cnt, ans)
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
#print(arr)
print(ans)