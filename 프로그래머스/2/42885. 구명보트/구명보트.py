from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    q = deque(people)
    while len(q) > 1:
        if q[-1] + q[0] <= limit:
            answer+=1
            q.popleft()
            q.pop()
        else:
            answer+=1
            q.popleft()
    if q:
        answer+=1
    return answer
