def main():
    for TC in range(int(input())):
        G, L = map(int, input().split())
        gas_stations = list(map(int, input().split()))
        print(G, L)
        print(gas_stations)


if __name__ == '__main__':
    main()
