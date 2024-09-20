def solution(money):
    answer = 0
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    #1. 처음 집은 무조건 턴다
    dp1[0] = money[0]
    for i in range(1, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    #2. 처음 집을 무조건 안턴다.
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    answer = max(dp2[-1], dp1[-2])
    return answer