def solution(data, ext, val_ext, sort_by):
    ind = ["code", "date", "maximum", "remain"]
    ind_num  = 0
    ans = []
    for i in range(len(ind)):
        if ind[i] == ext:
            ind_num = i
            break
    for da in data:
        if da[ind_num] < val_ext:
            ans.append(da)
    for i in range(len(ind)):
        if ind[i] == sort_by:
            ind_num = i
            break
    ans.sort(key =  lambda x : x[ind_num])
    return ans