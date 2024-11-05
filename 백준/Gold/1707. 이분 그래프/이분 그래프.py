import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

t = int(input())

def dfs(v, color):
    visit[v] =  color
    for i in tree[v]:
        if visit[i] == 0:
            if dfs(i, -color):
                pass
            else:
                return False
        elif visit[i] == visit[v]:
            return False
    return True


for times in range(t):
    v, e = map(int, input().split())
    tree = [[] for i in range(v+1)]
    visit = [0] *(v+1)
    for i in range(e):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    biapartite  = True
    for i in range(1, v+1):
        if visit[i] == 0:
            biapartite = dfs(i, 1)
            if not biapartite:
                break
    if biapartite:
        print("YES")
    else:
        print("NO")

