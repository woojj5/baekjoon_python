def solution(players, callings):
    answer = []
    res = {players[i]:i for i in range(len(players))}
    for c in callings:
        idx = res[c]
        res[c]-=1
        res[players[idx-1]] +=1
        players[idx-1], players[idx] = players[idx], players[idx-1] 
    return players