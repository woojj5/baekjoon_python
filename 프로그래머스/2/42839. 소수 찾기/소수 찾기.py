import math
def solution(numbers):
    ans_list = []
    def prime(n):
        if n in ans_list:
            return False
        ans_list.append(n)
        if n<2:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False

        return True

    def dfs(s, others):
        global answer
        if s != '':
            if prime(int(s)):
                answer+=1
        for i in range(len(others)):
            dfs(s+others[i], others[:i]+others[i+1:])
    global answer
    answer = 0   
    dfs("", numbers)
    return answer