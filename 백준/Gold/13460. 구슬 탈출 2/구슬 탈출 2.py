from collections import deque
import sys
input = sys.stdin.readline # 빠른 입출력 위한 코드
n,m=  map(int, input().split())
rx = ry = bx = by = -1  # 초기값 설정
table = []
for i in  range(n):
    table.append(list(input()))
    for j in range(m):
        if table[i][j] == 'R': # 빨간구슬 위치
            rx, ry = i, j
        elif table[i][j] == 'B': # 파란구슬 위치
            bx, by = i, j

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx,  by))
    visit = []
    count = 0
    visit.append((rx, ry, bx,  by))
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if count > 10 :
                print(-1)
                return
            if table[rx][ry] == "O":
                print(count)
                return
            for i in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nrx, nry = rx, ry
                while True:
                    nrx+= i[0]
                    nry+= i[1]
                    if not (0 <= nrx < n and 0 <= nry < m) or table[nrx][nry] == '#':
                        nrx -= i[0]
                        nry -= i[1]
                        break
                    if table[nrx][nry]  == "O":
                        break
                nbx, nby = bx, by
                while True:
                    nbx += i[0]
                    nby += i[1]
                    if not (0 <= nbx < n and 0 <= nby < m) or table[nbx][nby] == '#':
                        nbx -= i[0]
                        nby -= i[1]
                        break
                    if table[nbx][nby] == "O":
                        break
                if table[nbx][nby] == "O":
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx  - rx) + abs(nry  - ry) >  abs(nbx  - bx) + abs(nby  - by):
                        nrx-=i[0]
                        nry-=i[1]
                    else:
                        nbx -= i[0]
                        nby -= i[1]
                if (nrx, nry, nbx, nby) not in visit:
                    q.append((nrx, nry, nbx, nby))
                    visit.append((nrx, nry, nbx, nby))
        count+=1
    print(-1)
bfs(rx, ry, bx, by)