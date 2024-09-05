def solution(participant, completion):
    dicta = {}
    for i in participant:
        if i not in dicta:
            dicta[i] = 1
        else:
            dicta[i] +=1
    for i in completion:
        if i in dicta and dicta[i] > 0:
            dicta[i]-=1
    answer = list()
    
    for i in dicta.keys():
        if dicta[i] != 0:
            answer.append(i)
    answer = "".join(answer)
    return answer