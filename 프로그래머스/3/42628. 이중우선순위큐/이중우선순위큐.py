import heapq

def solution(operations):
    answer = []
    heap = []
    for op in operations:
        x,num = op.split()
        num = int(num)
        if x == "I":
            heapq.heappush(heap, num)
        elif x == "D" and num == 1:
            if len(heap) != 0:
                heap.remove(max(heap))
        else:
            if len(heap) != 0:
                heap.remove(min(heap))    
    if len(heap) == 0:
        answer = [0,0]
    else:
        answer = [max(heap), min(heap)]
    return answer