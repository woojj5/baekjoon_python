from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([0])
    for n in numbers:
        temp = deque()
        for x in q:
            temp.append(x+n)
            temp.append(x-n)
        q = temp
    for i in q:
        if target == i:
            answer+=1
    return answer