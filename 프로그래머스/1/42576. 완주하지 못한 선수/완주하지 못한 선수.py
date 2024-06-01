def solution(participant, completion):
    dict = {}
    for i in participant:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i]+=1
    for i in completion:
        dict[i] -=1
    for i in dict:
        if dict[i] > 0:
            answer = i
            break
    return answer