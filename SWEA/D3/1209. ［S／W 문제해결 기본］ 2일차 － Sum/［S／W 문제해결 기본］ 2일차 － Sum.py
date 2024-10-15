T = 10
for t in range(1, T+1):
    _ = int(input())
    N = 100
    arr = [list(map(int, input().split())) for i in range(N)]
    s1,s2, ans = 0,0,0
    for i in range(N):
        s1 += arr[i][i]
        s2 += arr[i][N-1-i]
        s3,s4 = 0,0
        for j in range(N):
            s3 += arr[i][j]
            s4 += arr[j][i]
        ans = max(ans, s3, s4)
    ans = max(ans, s1, s3)
    print(f'#{t} {ans}')