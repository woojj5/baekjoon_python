def solution(priorities, location):
    la = [(i,j) for i,j in enumerate(priorities)]
    answer = 0
    while True:
        cur = la.pop(0)
        if any(cur[1] < l[1] for l in la):
            la.append(cur)
        else:
            answer+=1
            if cur[0] == location:
                break
    return answer