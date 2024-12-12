def solution(edges):
    answer = [0,0,0,0]
    graph = {}
    for a,b in edges:
        if not graph.get(a):
            graph[a] = [0,0]
        if not graph.get(b):
            graph[b] = [0,0]
        graph[a][0]+=1
        graph[b][1]+=1
    
    for key, value in graph.items():
        if value[0] >= 2 and value[1] == 0:
            answer[0] = key
        elif value[0] >= 2 and value[1] >= 2:
            answer[3]+=1
        elif value[0] == 0 and value[1] > 0:
            answer[2]+=1
    answer[1] = graph[answer[0]][0]- answer[2] - answer[3]
        
    return answer