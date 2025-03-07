N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = N//2
ans = int(1e9)

visit = [0] * N

def dfs():
    global ans
    asm = bsm = 0
    for i in range(N):
        for j in range(N):
            if visit[i] and visit[j]:
                asm += arr[i][j]
            elif not visit[i] and not visit[j]:
                bsm += arr[i][j]
    ans = min(ans, abs(asm - bsm))
    return
def iter(it):
    if it == N:
        dfs()
        return
    visit[it] = 1
    iter(it+1)
    visit[it] = 0
    iter(it+1)
iter(0)
print(ans)