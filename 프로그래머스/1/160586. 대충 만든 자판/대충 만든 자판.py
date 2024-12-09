def solution(keymap, targets):
    dict1  = {}
    for key in keymap:
        for v,k in enumerate(key):
            if k not in dict1:
                dict1[k] = v+1
            else:
                dict1[k] = min(dict1[k], v+1)
    answer = []
    for tar in targets:
        tmp = 0
        for v in tar:
            if v not in dict1:
                tmp = -1
                break
            tmp+= dict1[v]
        answer.append(tmp)
    return answer