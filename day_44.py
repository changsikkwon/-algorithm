""" 다리를 지나는 트럭

    문제 설명: 
        트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다.
        모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
        트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
        ※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

        solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다.
        이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.
        
    입출력 예:
        bridge_length	weight	truck_weights	                return
        2	            10	    [7,4,5,6]	                    8
        100	            100	    [10]	                        101
        100	            100	    [10,10,10,10,10,10,10,10,10,10]	110
"""

def solution(bridge_length, weight, truck_weights):
    on_bridge = [0]*bridge_length
    
    while truck_weights:
        if sum(on_bridge)- on_bridge[0] + truck_weights[0] > weight:
            on_bridge.pop(0)
            on_bridge.append(0)
            bridge_length += 1
        else:
            on_bridge.pop(0)
            on_bridge.append(truck_weights.pop(0))
            bridge_length += 1
    return bridge_length