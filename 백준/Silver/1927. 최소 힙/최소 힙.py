import heapq
import sys
input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    a = int(input())
    if not a:
        if q:print(heapq.heappop(q))
        else:print(0)
    else:heapq.heappush(q, a)