import heapq
n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))
res = 0
for _ in range(n-1):
    a = heapq.heappop(arr) + heapq.heappop(arr)
    res+=a
    heapq.heappush(arr, a)
print(res)

