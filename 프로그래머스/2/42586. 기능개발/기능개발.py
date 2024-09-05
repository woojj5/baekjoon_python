def solution(progresses, speeds):
    import math
    answer = []
    days = [math.ceil((100 - i)/j) for i,j in zip(progresses, speeds) ]
    f,b = 0,0
    for i in range(len(days)):
        if days[i] > days[f]:
            answer.append(i-f)
            f = i
    answer.append(len(days) - f)
    return answer