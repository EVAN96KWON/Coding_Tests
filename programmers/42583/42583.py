def solution(bridge_length, weight, truck_weights):
    clock = 1
    bridge = [0 for _ in range(bridge_length)]

    # first truck goes to bridge at first
    next_truck = truck_weights.pop(0)
    sum_bridge = next_truck
    bridge[-1] = next_truck

    while truck_weights or sum_bridge:
        # trucks on bridge go forward
        sum_bridge -= bridge.pop(0)
        bridge.extend([0])

        # truck goes to bridge
        if truck_weights and truck_weights[0] + sum_bridge <= weight:
            next_truck = truck_weights.pop(0)
            sum_bridge += next_truck
            bridge[-1] = next_truck

        clock += 1

    return clock


if __name__ == '__main__':
    print(solution(2, 10, [7, 4, 5, 6]))  # 8
    print(solution(100, 100, [10]))  # 101
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110
