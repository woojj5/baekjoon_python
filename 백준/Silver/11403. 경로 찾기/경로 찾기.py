from collections import deque

def bfs(s):
    q = deque([s])
    while q:
        now = q.popleft()
        for i in range(len(graph[now])):
            if graph[now][i] == 1 and arr[i] == 0:
                q.append(i)
                arr[i] = 1

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    arr = [0] *n
    bfs(i)
    for j in range(n):
        print(arr[j], end = " ")
    print()
