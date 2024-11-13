import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def dfs(node, cnt):
    visit[node] = 1
    for a in graph[node]:
        if visit[a] == 0:
            cnt = dfs(a, cnt+1)
    return cnt
it = int(input())
for t in range(it):
    n,m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    visit = [0] * (n+1)
    for i in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(dfs(1,0))