def solution(s):
    answer = False
    cnt = 0
    for i in s:
        if i == '(':
            cnt +=1
        elif i == ')' and cnt >0:
            cnt -=1
        elif i == ')' and cnt == 0:
            return answer
    if cnt == 0:
        answer = True
    return answer