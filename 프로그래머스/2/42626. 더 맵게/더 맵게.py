def solution(scoville, K):
    answer = 0
    import heapq
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while heap[0] < K:
        heapq.heappush(heap, heapq.heappop(heap) + 2 * heapq.heappop(heap))
        answer+=1
        
        if len(heap) == 1 and heap[0] < K:
            return -1
    #print(scoville)
    return answer