def solution(wallet, bill):
    wl,wr = wallet
    bl,br = bill
    answer = 0
    while wl<bl or wr < br:
        if bl < br:
            br//=2
        else:
            bl//=2
        answer+=1
        if bl <= wr and br <= wl:
            break
    return answer