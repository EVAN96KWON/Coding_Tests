if __name__ == '__main__':
    count = 0
    target = input()
    keyword = input()

    while keyword in target:
        target = target[target.find(keyword) + len(keyword):]
        count = count + 1

    print(count)
