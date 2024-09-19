def solution(n, lost, reserve):
    answer = 0
    shirt = [1] * (n+1)
    for i in lost:
        shirt[i]-=1
    for i in reserve:
        shirt[i]+=1
    for i in range(1, n+1):
        if shirt[i] == 0:
            if i -1 >0 and shirt[i-1] > 1:
                shirt[i] =1
                shirt[i-1] =1
            elif i +1 <n+1 and shirt[i+1] > 1:
                shirt[i] =1
                shirt[i+1] =1
    for i in shirt:
        if i >0:
            answer+=1
    answer-=1
    return answer