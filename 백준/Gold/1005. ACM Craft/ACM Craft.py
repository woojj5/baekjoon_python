from collections import deque

ter = int(input())
for t in range(ter):
    n, m = map(int, input().split())
    value = [0] + list(map(int, input().split()))
    graph = [[] for i in range(n+1)]
    level = [0 for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        level[b]+=1
    fin_node = int(input())
    q = deque([])
    dp = [0 for i in range(n+1)]

    for i in range(1, n+1):
        if level[i] == 0:
            q.append(i)
            dp[i] = value[i]
    while q:
        now = q.popleft()
        for fut in graph[now]:
            dp[fut]  = max(dp[fut], dp[now] + value[fut])
            level[fut]-=1
            if level[fut] == 0:
                q.append(fut)

        if level[fin_node] == 0:
            print(dp[fin_node])
            break
