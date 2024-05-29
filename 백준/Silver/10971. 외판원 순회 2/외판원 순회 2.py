def dfs(x,y,start, cnt):

    if visit[x][y] != 0:
        return visit[x][y]
    
    if cnt == n:
        return 0
    
    ret = 100000000
    for i in range(n):
        if y & (1<< i) != 0 or arr[x][i] == 0:
            continue

        if (i != start and cnt == n-1) or (i == start and cnt !=n-1):
            continue

        ret = min(ret, arr[x][i] + dfs(i, y | (1 << i), start, cnt+1))

    visit[x][y] = ret
    return visit[x][y]

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
visit = [[0 for i in range(1<< n)] for i in range(n)]
print(dfs(0,0,0,0))