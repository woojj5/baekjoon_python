n = int(input())
m = int(input())
INF = int(1e10)
graph = [[] for i in range(n+1)]
distance= [INF] * (n+1)
visit = [0] * (n+1)
for i in range(m):
    w,e,h= map(int,input().split())
    graph[w].append((h,e))
    graph[e].append((h,w))

def prim(s):
    distance[s] = 0
    for _ in range(n): #1~n까지 전부 다 최적화를 진행해준다.
        mn = INF
        l_min = 0
        for i in range(1, n+1):
            if not visit[i] and distance[i] < mn:
                mn = distance[i]
                l_min = i
        visit[l_min] = 1

        for w, e in graph[l_min]:
            if not visit[e] and distance[e] > w:
                distance[e] = w
    print(sum(distance[1:]))

prim(1)
