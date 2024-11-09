n = int(input())
graph = list(map(int, input().split()))

def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)
count= 0
k = int(input())
dfs(k, graph)
for i in range(len(graph)):
    if graph[i] != -2 and i not in graph:
        count+=1
print(count)