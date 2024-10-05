import heapq
for _ in range(int(input())):
    n = int(input())
    num_list = list()
    for i in range((n-1)//10 + 1):
        num_list += list(map(int, input().split()))
    left_q, right_q, ans  = list(), list(), list()
    left_q.append(-num_list[0])
    ans.append(num_list[0])
    for i in range(1, n):
        if -left_q[0] < num_list[i]:
            heapq.heappush(right_q, num_list[i])
        else:
            heapq.heappush(left_q, -num_list[i])
        while len(left_q) - len(right_q) > 1:
            heapq.heappush(right_q, -heapq.heappop(left_q))
        while len(left_q) - len(right_q) < 0:
            heapq.heappush(left_q, -heapq.heappop(right_q))
        if not i % 2:
            ans.append(-left_q[0])
    print(len(ans))
    for i in range(0, len(ans), 10):
        print(*ans[i: min(i+10, len(ans))])