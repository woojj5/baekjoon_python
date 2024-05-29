import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
#print(n)
for i in range(n):
    a,b = map(int, input().rstrip().split())
    visit = [0 for i in range(10001)]
    visit[a] = 1
    q = deque()
    q.append((a, ""))
    while q:
        num, pr = q.popleft()
        if num == b:
            print(pr)
            break
        s =  (num -1) % 10000
        d =  num *2 % 10000
        l =  10 * (num % 1000) + num // 1000
        r =  1000 * (num % 10) + num // 10

        if not visit[d]:
            visit[d] = 1
            q.append((d, pr + "D"))
        if not visit[l]:
            visit[l] = 1
            q.append((l, pr + "L"))
        if not visit[r]:
            visit[r] = 1
            q.append((r, pr + "R"))
        if not visit[s]:
            visit[s] = 1
            q.append((s, pr + "S"))
    