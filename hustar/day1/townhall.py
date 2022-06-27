def main():
    for TC in range(int(input())):
        town = list(map(int, input().split()))
        cost = sum([abs(t - town[len(town) // 2]) for t in list(map(int, input().split()))])
        print(cost)


if __name__ == '__main__':
    main()
