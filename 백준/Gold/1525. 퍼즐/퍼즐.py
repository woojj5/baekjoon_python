from collections import deque
lista = ""
for i in range(3):
    lista += "".join(list(input().split()))
visited  = {lista: 0}
dx = [1,-1,0,0]
dy = [0,0,-1, 1]

def bfs():
    q = deque()
    q.append(lista)
    while q:
        puzzle = q.popleft()
        cnt = visited[puzzle]
        z = puzzle.index('0')
        if puzzle == '123456780':
            return  cnt

        x = z//3
        y = z%3
        cnt+=1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <= 2 and 0<= ny <=2:
                nz = 3*nx + ny
                puzzle_list = list(puzzle)
                puzzle_list[nz], puzzle_list[z] = puzzle_list[z], puzzle_list[nz]
                new_puzzle = ''.join(puzzle_list)

                if visited.get(new_puzzle, 0) == 0:
                    visited[new_puzzle] = cnt
                    q.append(new_puzzle)
    return -1

print(bfs())
