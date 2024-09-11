from collections import deque
def check(start, end, visited, graph):
    visited[start] = 1
    visited[end] = 1
    q = deque()
    cnt = 1
    q.append(end)
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                cnt+=1
                q.append(next)
    return cnt
def solution(n, wires):
    answer = float("inf")
    graph = [[] for i in range(n+1)]
    for i,j in wires:
        graph[i].append(j)
        graph[j].append(i)
    for i,j in wires:
        visited = [0] * (n+1)
        res = check(i,j, visited, graph)
        alpha = abs(n - res)
        res = abs(res - alpha)
        answer = min(res, answer)
    return answer