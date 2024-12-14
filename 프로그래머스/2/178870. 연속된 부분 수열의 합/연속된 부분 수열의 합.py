def solution(sequence, k):
    answer = []
    s,e = 0,0
    size = len(sequence)
    temp = sequence[0]
    min_len = 1000001
    while s<=e<size:
        if temp == k:
            if e-s+1<min_len:
                min_len = e-s+1
                answer = [s,e]
            temp-=sequence[s]
            s+=1
        elif temp < k:
            e+=1
            if e < size:
                temp+=sequence[e]
        elif temp > k:
            temp -= sequence[s]
            s+=1
                
    return answer