from collections import deque
import sys
input = sys.stdin.readline

start, target = map(int, input().split())
q = deque()
q.append((start, 1))

while q:
    n, c = q.popleft()
    if n == target:
        print(c)
        break
    if n * 2 <= target:
        q.append((n * 2, c + 1))
    if n * 10 + 1 <= target:
        q.append((n * 10 + 1, c + 1))
else:
    print(-1)
