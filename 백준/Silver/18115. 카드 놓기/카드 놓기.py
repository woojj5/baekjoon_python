from collections import deque

# 입력 받기
N = int(input())
A = list(map(int, input().split()))
A.reverse()
# 덱을 사용해 초기 카드 상태를 복원
initial_cards = deque()

# N부터 1까지 역순으로 카드를 넣는 과정
for i in range(N):
    if A[i] == 1:
        initial_cards.appendleft(i+1)  # 제일 위에 카드 추가
    elif A[i] == 2:
        initial_cards.insert(1, i+1)
    elif A[i] == 3:
        initial_cards.append(i+1)      # 제일 아래에 카드 추가
print(' '.join(map(str, initial_cards)))