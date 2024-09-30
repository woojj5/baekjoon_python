from collections import deque

def bfs(s, e):
    q = deque([s])  # 시작점을 큐에 추가합니다
    visit[s] = 0  # 시작점에서의 시간은 0

    while q:
        x = q.popleft()
        
        # 목표점에 도달하면 visit[x] 리턴
        if x == e:
            return visit[x]
        
        # x에서 이동할 수 있는 세 가지 경우: x-1, x+1, x*2
        for i in (x - 1, x + 1, x * 2):
            # i가 범위 안에 있고, 아직 방문하지 않은 경우
            if 0 <= i < limit and visit[i] == -1:
                if i == x * 2:  # 순간 이동일 때는 시간 변화 없음
                    visit[i] = visit[x]
                    q.appendleft(i)  # 순간 이동은 우선적으로 처리
                else:  # 한 칸 이동일 때는 시간이 1 증가
                    visit[i] = visit[x] + 1
                    q.append(i)

s, e = map(int, input().split())
limit = 100001  # 범위 설정
visit = [-1] * limit  # 방문 기록을 -1로 초기화 (미방문 상태)

# bfs 결과 출력
print(bfs(s, e))
