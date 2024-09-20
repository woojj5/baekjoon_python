def solution(triangle):
    answer = 0
    #1. 처음 값은 무조건 고른다
    #2. 다음 값은 둘중에 하나를 고른다
    #3. 해당 위치 or 위치 +1을 고른다
    #3. 그 중에서 가장 최대값인 것을 고른다.
    tri = [[0 for i in range(len(triangle))] for i in range(len(triangle))]
    #print(tri)
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i == 0:
                tri[i][j] = triangle[0][0]
            else:
                if j > 0:
                    tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + triangle[i][j]
                else:
                    tri[i][j] = tri[i-1][j] + triangle[i][j]
    answer = max(tri[-1])                
        
    return answer