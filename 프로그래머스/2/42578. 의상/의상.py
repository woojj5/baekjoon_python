def solution(clothes):
    answer = 1
    dict1 = dict()
    for i,j in clothes:
        if j not in dict1:
            dict1[j] = 1
        else:
            dict1[j]+=1
    for i in dict1.values():
        answer *= (int(i)+1) 
    answer-=1
    return answer