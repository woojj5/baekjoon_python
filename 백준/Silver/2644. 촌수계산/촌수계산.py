n = int(input())
start, target = map(int, input().split())
m = int(input())
res = []
arr = [[] for i in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    v,e = map(int, input().split())
    arr[v].append(e)
    arr[e].append(v)
def dfs(x, cnt):
    cnt+=1
    visited[x] = 1
    if x == target:
        res.append(cnt)
    for i in arr[x]:
        if visited[i] == 0:
            dfs(i, cnt)
dfs(start, 0)
if len(res) == 0:
    print(-1)
else:
    print((res[0])-1)
