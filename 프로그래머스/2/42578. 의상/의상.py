def solution(clothes):
    dicta = {}
    for _,i in clothes:
        if i not in dicta:
            dicta[i] = 1
        else:
            dicta[i] += 1
    answer = 1
    for i in dicta.values():
        answer = (answer) * (i+1)
    answer -=1
    return answer