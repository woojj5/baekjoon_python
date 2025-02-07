import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
chicken = []
people = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i,j))
        elif arr[i][j] == 1:
            people.append((i,j))
#각각의 위치를 찾음.
visit = [0] * len(chicken)
res = int(1e9)
def dfs(idx, cnt):
    global res
    if cnt == m:
        ans = 0
        for p in people:
            dis = int(1e9)
            for i in range(len(visit)):
                if visit[i]:
                    distance = abs(chicken[i][0] - p[0]) + abs(chicken[i][1] - p[1])
                    dis = min(dis, distance)
            ans+= dis
        res = min(ans, res)

    for i in range(idx, len(chicken)):
        if not visit[i]:
            visit[i] = 1
            dfs(i+1, cnt+1)
            visit[i] = 0

dfs(0, 0)
print(res)