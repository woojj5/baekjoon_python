from collections import deque
n, s, g, u, d = map(int, input().split())


def bfs(start, goal, up, down, max_iter):
    q = deque()
    q.append([start, 0])
    visit = [0] * (max_iter+1)
    visit[s] = 1
    while q:
        cur_start, count = q.popleft()
        if cur_start == goal:
            return count

        next_floor = cur_start + up
        if next_floor <= max_iter and visit[next_floor] == 0:
            visit[next_floor] = 1
            q.append([next_floor, count+1])

        next_floor = cur_start - down
        if next_floor >0 and visit[next_floor] == 0:
            visit[next_floor] = 1
            q.append([next_floor, count+1])
    return "use the stairs"
print(bfs(s,g,u,d,n))
