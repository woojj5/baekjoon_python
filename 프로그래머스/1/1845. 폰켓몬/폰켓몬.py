def solution(nums):
    answer = 0
    l = len(nums)//2
    s = set(nums)
    if l <= len(s):
        answer  = l
    else:
        answer = len(s)
    return answer