from bisect import bisect_left, bisect_right
from collections import defaultdict
def solution(words, queries):
    word_dict = defaultdict(list)
    reverse_dict=  defaultdict(list)
    answer = []
    for w in words:
        word_dict[len(w)].append(w)
        reverse_dict[len(w)].append(w[::-1])
    for key in word_dict.keys():
        word_dict[key].sort()
        reverse_dict[key].sort()
    
    for q in queries:
        if q[0] == '?':
            q = q[::-1]
            s,e = q.replace('?', 'a'), q.replace('?', 'z')
            lst = reverse_dict[len(q)]
        else:
            s,e = q.replace('?', 'a'), q.replace('?', 'z')
            lst = word_dict[len(q)]
        answer.append(bisect_right(lst, e) - bisect_left(lst, s))
    
    return answer