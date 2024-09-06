def solution(citations):
    ch = 0
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        hindex = len(citations) - i
        if citations[i] >= hindex:
            answer = hindex
            break
            
    return answer