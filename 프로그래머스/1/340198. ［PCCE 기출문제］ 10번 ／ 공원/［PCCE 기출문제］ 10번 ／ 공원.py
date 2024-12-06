def solution(mats, park):
    def check_area(x,y,s):
        cnt = 0
        for i in range(x, x+s):
            for j in range(y, y+s):
                if i < len(park) and j < len(park[0]):
                    if park[i][j] != "-1":
                        return False
                else:
                    return False
        return True
    mats.sort(reverse = True)
    for m in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if check_area(i,j,m):
                    return m
    return -1