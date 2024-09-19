from collections import deque

def solution(people, limit):
    q = deque(sorted(people, reverse = True))
    answer = 0
    
    while len(q) >1:
        if q[0] + q[-1] <= limit:
            q.pop()
            q.popleft()
            answer+=1
        else:
            answer+=1
            q.popleft()
        
    if q:
        answer+=1
    return answer