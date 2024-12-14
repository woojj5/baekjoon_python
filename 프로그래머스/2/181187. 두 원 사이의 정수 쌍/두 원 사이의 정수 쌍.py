import math
def solution(r1, r2):
    ans = 0
    for i in range(1, r2+1):
        y_max = math.floor(math.sqrt(r2*r2 - i*i))
        y_min = 0 if i > r1 else math.ceil(math.sqrt(max(0,r1*r1 - i*i)))
        ans += (y_max - y_min+1)
    return 4* ans