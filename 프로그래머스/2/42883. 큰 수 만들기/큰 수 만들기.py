from itertools import permutations

def solution(number, k):
    st = []
    cnt = k
    for i in number:
        while st and cnt and st[-1] < i:
            st.pop()
            cnt-=1
        st.append(i)
    return ''.join(st[:len(number) - k])