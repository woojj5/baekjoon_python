import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, group):
    visit[x] = group
    for i in graph[x]:
        if not visit[i]:
            a = dfs(i, -group)
            if not a:
                return False
        elif visit[i] == visit[x]:
            return False
    return True

k = int(input())
for _ in range(k):
    n,m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    visit = [0] * (n+1)
    for i in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, n+1):
        if not visit[i]:
            res = dfs(i,1)
            if not res:
                break
    if res:
        print("YES")
    else:
        print("NO")