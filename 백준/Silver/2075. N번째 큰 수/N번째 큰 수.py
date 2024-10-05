import heapq

heap = []

n = int(input())
for i in range(n):
    num = map(int, input().split())
    for nu in num:
        if len(heap) < n:
            heapq.heappush(heap, nu)
        else:
            if heap[0] < nu:
                heapq.heappop(heap)
                heapq.heappush(heap, nu)
print(heap[0])