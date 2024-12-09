def solution(park, routes):
    answer = []
    w,h = len(park[0]),len(park)
    for i,p in enumerate(park):
        for j,x in enumerate(p):
            if x == "S":
                answer = [i,j]
                break
    for route in routes:
        a,b = route.split()
        if a == 'E':
            if answer[1]+int(b)<w:  
                if 'X' not in park[answer[0]][answer[1]:answer[1]+int(b)+1]:  
                    answer[1] += int(b)

        elif a == 'W':
            if answer[1]-int(b)>=0:
                if 'X' not in park[answer[0]][answer[1]-int(b):answer[1]+1]:
                    answer[1] -= int(b)

        elif a == 'N':
            if answer[0]-int(b)>=0:
                if 'X' not in [ch[answer[1]] for ch in park[answer[0]-int(b):answer[0]+1]]:
                    answer[0] -= int(b)

        else:   # 남쪽 
            if answer[0]+int(b)<h:
                if 'X' not in [ch[answer[1]] for ch in park[answer[0]:answer[0]+int(b)+1]]:
                    answer[0] += int(b)

    return answer