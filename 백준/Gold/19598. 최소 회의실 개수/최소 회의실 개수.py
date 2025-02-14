import heapq

n = int(input())
stack = []
res = []
for _ in range(n):
    a,b = map(int, input().split())
    res.append((a,b))
res.sort()
heapq.heappush(stack, res[0][1])
for i in range(1, n):
    if stack[0] <= res[i][0]:
        heapq.heappop(stack)
    heapq.heappush(stack, res[i][1])
print(len(stack))