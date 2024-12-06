def solution(friends, gifts):
    answer = 0
    giftdict = {k:{j:0 for j in friends if j!= k} for k in friends}
    gives = {k:0 for k in friends}
    gets = {k:0 for k in friends}
    for item in gifts:
        send, receive = item.split(" ")
        giftdict[send][receive] +=1
        gives[send]+=1
        gets[receive]+=1
    ans = 0    
    for k,v in giftdict.items():
        cnt = 0
        for kk,vv in giftdict[k].items():
            if giftdict[k][kk] > giftdict[kk][k]:
                cnt+=1
            elif giftdict[k][kk] == giftdict[kk][k]:
                if gives[k] - gets[k] > gives[kk] - gets[kk]:
                    cnt+=1
        ans = max(ans, cnt)

        
    return ans