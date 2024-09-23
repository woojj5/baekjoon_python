def solution(n, lost, reserve):
    answer = 0
    uniform = [1] * (n+1)
    uniform[0] = 0
    for i in lost:
        uniform[i]-=1
    for i in reserve:
        uniform[i]+=1
   # print(uniform)
    for i in range(1, n+1):
        if uniform[i] == 0:
            if i-1 > 0 and uniform[i-1] == 2:
                uniform[i-1] = 1
                uniform[i] = 1
            elif i+1 < n+1 and uniform[i+1] == 2:
                uniform[i+1] = 1
                uniform[i] = 1
    #print(uniform)
    for i in uniform:
        if i > 0:
            answer+=1
    return answer