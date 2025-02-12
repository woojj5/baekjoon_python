import heapq
n,m,k = map(int, input().split())
arr = []
for _ in range(k):
    v,c = map(int, input().split())
    arr.append((v,c))

arr.sort(key= lambda x: x[1])
preference = 0
q = []
res = int(1e9)
for a in arr:
    heapq.heappush(q, a)
    preference += a[0]
    if len(q) >= n:
        if preference >= m:
            print(a[1])
            exit(0)
        else:
            preference -= heapq.heappop(q)[0]
print(-1)