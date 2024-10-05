from collections import deque
n = int(input())
card = deque([i+1 for i in range(n)])
while len(card) > 1:
    card.popleft()
    a = card.popleft()
    card.append(a)
for i in card:
    print(i)