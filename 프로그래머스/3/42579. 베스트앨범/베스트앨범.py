def solution(genres, plays):
    dic1 = {}
    dic2 = {}
    for i, (g,p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i,p)]
        else:
            dic1[g].append((i,p))
        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    #dic1 은 g에  1,p가 존대
    #dic2는 g에 p의 합만 존재
    answer = []
    for (g,v) in sorted(dic2.items(), key = lambda x: x[1], reverse = True):
        for (i,p) in sorted(dic1[g], key = lambda x: x[1], reverse = True)[:2]:
            answer.append(i)
    
    
    return answer