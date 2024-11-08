import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())

graph = [[] for i in range(n+1)]
arr = [-1] * (n+1)
arr[1] = 0
for i in range(n-1):
    h,e, w = map(int, input().split())
    graph[h].append((e, w))
    graph[e].append((h, w))


def dfs(x, weight):
    for i in graph[x]:
        a,b = i
        if arr[a] == -1:
            arr[a] = b + weight
            dfs(a, b+ weight)
dfs(1,0)
start = arr.index(max(arr))
arr = [-1] * (n+1)
arr[start] = 0
dfs(start, 0)
print(max(arr))