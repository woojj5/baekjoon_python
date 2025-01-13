def solution(s):
    answer = True
    cnt = 0
    for i in s:
        for a in i:
            if a == 'p' or a == 'P':
                cnt+=1
            elif a == 'y' or a == 'Y':
                cnt-=1
    if cnt:
        return False
    return True