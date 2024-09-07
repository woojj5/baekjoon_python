def solution(answers):
    answer = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    score = [0,0,0]
    fir = [1,2,3,4,5]
    sec = [2,1,2,3,2,4,2,5]
    thir = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == fir[i%5]:
            score[0]+=1
        if answers[i] == sec[i%8]:
            score[1]+=1
        if answers[i] == thir[i%10]:
            score[2]+=1
            
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i+1)
    #print(answer)
    return sorted(answer)