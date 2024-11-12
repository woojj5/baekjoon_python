from collections import deque
s,e = map(int, input().split())
q = deque()
q.append(s)
visit = [0] * int(1e5+1)
check = [0] * int(1e5+1)
visit[s] = 0
cnt = 0
rem = []
def mov(now):
    data=  []
    temp = now
    for i in range(visit[now] + 1):
        data.append(temp)
        temp = check[temp]
    print(' '.join(map(str, data[::-1])))

while q:
    x = q.popleft()
    if x == e:
        print(visit[x])
        mov(x)
        break
    for nx in (x-1, x+1, 2*x):
        if 0<= nx<= 1e5 and visit[nx] == 0:
            visit[nx] = visit[x] + 1
            q.append(nx)
            check[nx] = x