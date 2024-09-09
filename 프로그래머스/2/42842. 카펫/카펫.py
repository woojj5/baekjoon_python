def solution(brown, yellow):
    answer = []
    max_num = brown + yellow
    x = y = 0
    for i in range(1, yellow+1):
        if yellow % i == 0:
            x = i
            y = yellow/i
            if 2* (x + y + 2) == brown:
                x+=2
                y+=2
                break
    answer.append(y)
    answer.append(x)   
    answer.sort(reverse=True)
    return answer