def solution(diffs, times, limit):
    answer = max(diffs)
    l,r = 1, max(diffs)
    while l< r:
        m = int((l+r)//2)
        s = times[0]
        for i in range(1, len(diffs)):
            k = 0
            if m < diffs[i]:
                k = diffs[i] - m
            s+= ((times[i]+ times[i-1]) * (k)+ times[i])
        
        if s<= limit:
            r = m
            answer = m
        elif s>= limit:
            l = m+1
        
    return answer