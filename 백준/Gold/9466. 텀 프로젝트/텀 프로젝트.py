import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)
def dfs(s):
    global num
    visit[s] = True
    sel = arr[s]
    team.append(s)
    if visit[sel]:
        if sel in team:
            num += len(team[team.index(sel):])
    else:
        dfs(sel)
it = int(input())
for t in range(it):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visit = [False] * (n+1)
    num = 0
    for i in range(1, n+1):
        if not visit[i]:
            team = []
            dfs(i)
    print(n-num)
