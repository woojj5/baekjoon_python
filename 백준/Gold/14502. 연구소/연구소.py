from collections import deque
import sys
input = sys.stdin.readline
import copy
def bfs():
    q = deque()
    test_copy = copy.deepcopy(lista)
    for i in range(n):
        for j in range(m):
            if test_copy[i][j] == 2:
                q.append((i,j))

    while q:
        r,c = q.popleft()
        for i in ((1,0), (-1, 0), (0, 1), (0, -1)):
            nr = r+i[0]
            nc = c+i[1]
            if 0<= nr < n and 0<= nc < m and test_copy[nr][nc] == 0:
                test_copy[nr][nc] = 2
                q.append((nr, nc))

    global res
    count = 0
    for i in range(n):
        for j in range(m):
            if test_copy[i][j] == 0:
                count+=1

    res = max(res, count)

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lista[i][j] == 0:
                lista[i][j] = 1
                make_wall(cnt+1)
                lista[i][j] = 0




n, m = map(int, input().split())
lista = [list(map(int, input().split())) for i in range(n)]
res = 0
make_wall(0)
print(res)