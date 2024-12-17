def solution(edges):
    answer = [0,0,0,0]
    max_num = 0
    for i,j in edges:
        max_num = max(max_num, max(i,j))
    print(max_num)
    in_ward = [ [] for i in range(max_num+1)]
    out_ward = [ [] for i in range(max_num+1)]
    for i,j in edges:
        out_ward[i].append(j)
        in_ward[j].append(i)

    for i in range(1, max_num+1):
        if len(out_ward[i]) >=2 and len(in_ward[i]) == 0:
            answer[0] = i
        elif len(out_ward[i]) ==0 and len(in_ward[i]) >=1:
            answer[2]+=1
        elif len(out_ward[i]) ==2 and len(in_ward[i]) >= 2:
            answer[3]+=1
    answer[1] = len(out_ward[answer[0]]) - answer[2] - answer[3]     
    
    return answer