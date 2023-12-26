def infect(computer):
    if infected[computer]:
        return

    infected[computer] = True
    for next_computer in network[computer]:
        infect(next_computer)


if __name__ == '__main__':
    network = {_: [] for _ in range(1, int(input()) + 1)}
    infected = [False] + [False] * len(network)
    nets = int(input())

    for net in range(nets):
        src, dst = map(int, input().split())
        network[src].append(dst)
        network[dst].append(src)

    infect(1)

    print(infected.count(True) - 1)


