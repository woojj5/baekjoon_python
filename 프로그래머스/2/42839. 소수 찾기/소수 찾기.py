from itertools import permutations
def prime(r):
    cnt = 0
    for i in range(2, int(r**0.5) + 1):
        if r % i == 0:
            cnt+=1
    if cnt == 0:
        return True
    else:
        return False

def solution(numbers):
    answer = 0
    res =[]
    for i in range(1, len(numbers) + 1):
        for c in list(permutations(numbers, i)):
            if int(''.join(c)) not in res and int(''.join(c)) not in (0,1):
                res.append(int(''.join(c)))
    
    for r in res:
        if prime(r):
            answer+=1
    return answer