
def solution(bridge_length, weight, truck_weights):
    trucks_in_bridge = [0 for _ in range(bridge_length)]
    time = 0
    total = 0
    while truck_weights or total:
        total -=trucks_in_bridge.pop(0)
        temp = 0
        if (len(truck_weights) > 0 and total + truck_weights[0] <= weight):
            temp = truck_weights.pop(0)
        total+=temp
        trucks_in_bridge.append(temp)
        time += 1
    
    return time

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))