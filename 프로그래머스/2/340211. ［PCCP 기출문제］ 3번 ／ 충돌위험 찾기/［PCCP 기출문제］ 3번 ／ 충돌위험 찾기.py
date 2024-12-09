from collections import Counter
def solution(points, routes):
    def bfs(route):
        idx = 0
        pa = []
        for i in range(len(route)-1):
            sx,sy = spot[route[i]-1]
            ex,ey = spot[route[i+1]-1]
            
            while sx != ex:
                pa.append((sx, sy, idx))
                if sx< ex:
                    sx+=1
                else:
                    sx-=1
                idx+=1
            while sy != ey:
                pa.append((sx, sy, idx))
                if sy< ey:
                    sy+=1
                else:
                    sy-=1
                idx+=1
        pa.append((sx, sy, idx))
        return pa
                    
    spot = [i for i in points]
    second = []
    for route in routes:
        second.extend(bfs(route))
    res = 0
    temp = Counter(second)
    for i in temp.values():
        if i >= 2:
            res+=1
    
    return res