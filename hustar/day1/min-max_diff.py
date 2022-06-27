def main():
    for t in range(int(input())):
        li = list(map(int, input().split()))
        print(max(li) - min(li))


if __name__ == '__main__':
    main()
