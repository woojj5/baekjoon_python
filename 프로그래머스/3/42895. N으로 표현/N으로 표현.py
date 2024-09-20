def solution(N, number):
    answer = -1
    dp = [set() for i in range(8)]
    for i in range(8):
        dp[i].add(int(str(N) * (i+1)))
    for i in range(8):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j-1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1//op2)
        if number in dp[i]:
            answer = i+1
            break
    return answer