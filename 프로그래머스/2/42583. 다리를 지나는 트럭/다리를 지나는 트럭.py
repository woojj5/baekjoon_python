def solution(bridge_length, weight, truck_weights):
    answer = 0 
    bridge = [0] * bridge_length
    curr = 0
    while len(truck_weights) > 0:
        answer +=1
        curr = curr -bridge.pop(0)
        
        if curr + truck_weights[0] <= weight:
            curr += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
    return answer+bridge_length