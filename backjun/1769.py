if __name__ == '__main__':
    X = input()
    count = 0

    while len(X) != 1:
        count += 1
        Y = 0
        for i in range(len(X)):
            Y += int(X[i])
        X = str(Y)

    print(count)
    if int(X) % 3 == 0:
        print("YES")
    else:
        print("NO")
