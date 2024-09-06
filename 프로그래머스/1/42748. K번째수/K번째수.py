def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        ind = array[commands[i][0]-1 : commands[i][1]]
        ind.sort()
        answer.append(ind[commands[i][2]-1])
        
    return answer