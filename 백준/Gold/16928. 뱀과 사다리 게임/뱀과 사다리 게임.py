from collections import deque
n,m = map(int, input().split())
ladder = [0] * 101  # 사다리 정보를 담을 리스트
snake = [0] * 101   # 뱀 정보를 담을 리스트
visit = [0] * 101 
for i in range(n):
    a,b = map(int, input().split())
    ladder[a] = b
for i in range(m):
    a,b = map(int, input().split())
    snake[a] = b

q = deque([1])
visit[1] =1
while q:
    x = q.popleft()
    if x == 100:
        print(visit[x]-1)
        break
    for i in range(1,7):
        nx = x + i
        if nx <= 100 and not visit[nx]:
            if ladder[nx]:
                nx = ladder[nx]
            if snake[nx]:
                nx = snake[nx]
            if not visit[nx]:
                visit[nx] = visit[x] + 1
                q.append(nx)