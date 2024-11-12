import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
visit = [False] * n
graph = [[] for i in range(n)]
arrive= False
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, depth):
    global arrive
    visit[start] = True
    if depth == 5:
        arrive = True
        return
    for i in graph[start]:
        if visit[i] == False:
            dfs(i, depth+1)
    visit[start] = False

for i in range(n):
    dfs(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)