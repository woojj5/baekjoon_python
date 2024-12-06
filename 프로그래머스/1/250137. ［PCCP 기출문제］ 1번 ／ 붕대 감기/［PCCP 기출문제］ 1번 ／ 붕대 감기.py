def solution(bandage, health, attacks):
    res = health
    cnt = 0
    ind = 0
    endt = attacks[-1][0]
    attacks = {attack[0]:attack[1] for attack in attacks}
    for i in range(1,  endt+ 1):
        if i in attacks:
            res-=attacks[i]
            cnt = 0
            if res<= 0:
                return -1
            continue
        cnt+=1
        res= res +bandage[1]
        if cnt == bandage[0]:
            res = res +bandage[2]
            cnt = 0
        res = min(res, health)
    return res