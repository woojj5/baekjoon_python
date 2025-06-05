from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# 입력
n, m, c = map(int, input().split())
s = list(map(int, input().split()))

# 그래프 생성 및 초기 설정
graph = defaultdict(list)
indegree = [0] * n
for _ in range(c):
    a, b, x = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, x))
    indegree[b] += 1

# dp[i] = earliest day session i can happen
dp = s[:]
q = deque(i for i in range(n) if indegree[i] == 0)

# 위상정렬 기반 갱신
while q:
    u = q.popleft()
    for v, cost in graph[u]:
        if dp[v] < dp[u] + cost:
            dp[v] = dp[u] + cost
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

# 출력
for val in dp:
    print(val)
