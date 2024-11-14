from collections import deque
t = int(input())
graph = [[] for i in range(t+1)]
cost = [0] * (t+1)
degree = [0] * (t+1)
ans = [0] * (t+1)
for it in range(1,t+1):
    lista = list(map(int, input().split()))
    cost[it] = lista[0]
    bs  = lista[1:-1]
    for i in bs:
        graph[i].append(it)
        degree[it]+=1
q = deque()
for i in range(1, t+1):
    if degree[i] == 0:
        ans[i] = cost[i]
        q.append(i)

while q:
    now = q.popleft()
    for n in graph[now]:
        degree[n]-=1
        ans[n]  = max(ans[n], ans[now] + cost[n])
        if degree[n] == 0:
            q.append(n)
print(*ans[1:], sep= '\n')