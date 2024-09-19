def solution(routes):
    answer = 0
    max_x = -30001
    routes.sort(key = lambda x : x[1])    
    for r in routes:
        if r[0]>max_x:
            max_x = r[1]
            answer+=1
    return answer