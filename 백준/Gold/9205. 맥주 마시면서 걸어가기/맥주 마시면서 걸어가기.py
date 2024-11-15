from collections import deque
def bfs():
    q = deque()
    q.append(s)
    while q:
        x,y = q.popleft()
        if abs(x- h[0]) + abs(y- h[1])<= 1000:
            print('happy')
            return
        for i in range(k):
            if not visit[i]:
                nx, ny = graph[i]
                if abs(x- nx) + abs(y- ny)<= 1000:
                    visit[i] = 1
                    q.append((nx, ny))
    print('sad')
    return

num = int(input())
for t in range(num):
    k = int(input())
    s = list(map(int, input().split()))
    graph = []
    for i in range(k):
        a,b = map(int, input().split())
        graph.append((a,b))

    h = list(map(int, input().split()))
    visit = [0] * (k+1)
    bfs()
