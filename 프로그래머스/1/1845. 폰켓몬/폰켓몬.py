def solution(nums):
    answer = 0
    ind = len(nums)//2
    dicta = {}
    for i in nums:
        if i not in dicta:
            dicta[i] = 1
        else:
            dicta[i]+=1
    lista = dicta.keys()
    if len(lista) < ind:
        answer  = len(lista)
    else:
        answer = ind
    return answer