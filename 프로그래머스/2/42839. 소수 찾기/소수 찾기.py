from itertools import permutations
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    temp = []
    
    for i in range(1, len(numbers)+1):
        temp += list(permutations(numbers, i)) 
    #print(temp)
    num = [int(''.join(t)) for t in temp] 
    ans = []
    for i in num:
        if prime(i):
            ans.append(i)
    return len(set(ans))
    