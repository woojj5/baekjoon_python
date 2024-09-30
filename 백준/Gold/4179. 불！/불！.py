from collections import deque

n, m = map(int, input().split())
arr = []
s = deque()  # 지훈이의 위치 큐
f = deque()  # 불의 위치 큐

# 방문 배열 초기화
visit1 = [[0] * m for _ in range(n)]
visit2 = [[0] * m for _ in range(n)]

for i in range(n):
    lista = list(input().strip())  # 문자열로 입력 받기
    for j in range(m):
        if lista[j] == 'J':
            s.append((i, j))  # 지훈이의 시작 위치
            visit1[i][j] = 1  # 지훈이의 방문 처리
        elif lista[j] == 'F':
            f.append((i, j))  # 불의 시작 위치
            visit2[i][j] = 1  # 불의 방문 처리
    arr.append(lista)

# 이동 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    # 불이 퍼지는 BFS
    while f:
        x, y = f.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visit2[nx][ny] and arr[nx][ny] != "#":
                    visit2[nx][ny] = visit2[x][y] + 1
                    f.append((nx, ny))
    
    # 지훈이의 BFS
    while s:
        x, y = s.popleft()
        # 경계 조건 검사 - 탈출 가능한지 확인
        if x == 0 or x == n-1 or y == 0 or y == m-1:
            return visit1[x][y]  # 탈출 성공
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] != "#" and not visit1[nx][ny]:
                    # 불보다 먼저 도착할 수 있는 경우
                    if not visit2[nx][ny] or visit2[nx][ny] > visit1[x][y] + 1:
                        visit1[nx][ny] = visit1[x][y] + 1
                        s.append((nx, ny))

    return "IMPOSSIBLE"  # 모든 경우를 시도했으나 탈출 불가능

result = bfs()
print(result)
