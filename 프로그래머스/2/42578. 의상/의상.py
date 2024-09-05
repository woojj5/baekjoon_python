def solution(clothes):
    dicta = {}
    for i in clothes:
        if i[1] not in dicta:
            dicta[i[1]] = 1
        else:
            dicta[i[1]] += 1
    answer = 1
    for i in dicta.values():
        answer = (answer) * (i+1)
    answer -=1
    return answer