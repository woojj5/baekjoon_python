for t in range(1, 11):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    mn = 10000
    for j in range(1, 101):
        if arr[0][j] == 0:
            continue
        cj = j
        cnt = d = ci = 0
        while ci < 99:
            cnt+=1
            if d == 0:
                ci+=1
                if arr[ci][cj-1] == 1:
                    d -=1
                elif arr[ci][cj+1] == 1:
                    d +=1
            else:
                cj += d
                if arr[ci][cj+d] == 0:
                    d = 0
        if mn >= cnt:
            mn = cnt
            ans = j-1
    print(f'#{t} {ans}')