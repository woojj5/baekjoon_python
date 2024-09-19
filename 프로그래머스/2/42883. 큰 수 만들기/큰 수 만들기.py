from itertools import permutations

def solution(number, k):
    #answer = ''
    stack = []
    for i in number:
        while stack and stack[-1] < i and k:
            stack.pop()
            k-=1
        stack.append(i)
    return ''.join(stack[:len(number)-k])