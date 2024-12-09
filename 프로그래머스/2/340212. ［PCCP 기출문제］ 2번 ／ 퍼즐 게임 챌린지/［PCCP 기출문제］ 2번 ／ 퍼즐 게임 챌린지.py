def solution(diffs, times, limit):
    l = 1
    r = max(diffs)
    answer = max(diffs)
    while l< r:
        mid = int((l + r) /2)
        time = times[0]
        
        for i in range(1, len(diffs)):
            k = 0
            if mid < diffs[i]:
                k = diffs[i] - mid
            time+=  (times[i] + times[i-1]) * k + times[i]
            
        if time <= limit:
            r = mid
            answer = mid
        else:
            l = mid+1
    return answer