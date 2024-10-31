from collections import deque

def sol(n, tree):
    q = deque([1])
    parent = [0] * (n+1)
    parent[1] = 1
    while q:
        now = q.popleft()
        for v in tree[now]:
            if v != 1 and parent[v] == 0:
                parent[v] = now
                q.append(v)

    for i in range(2,  n+1):
        print(parent[i])



n = int(input())
tree = dict()
for i in range(1, n+1):
    tree[i] = []
for i in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
sol(n, tree)