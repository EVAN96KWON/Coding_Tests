if __name__ == '__main__':
    today = dict()
    N = int(input())

    for n in range(N):
        book = input()
        if book in today:
            today[book] += 1
        else:
            today[book] = 1

    max_v = max(today.values())
    max_list = []

    for book, number in today.items():
        if number == max_v:
            max_list.append(book)

    print(sorted(max_list)[0])

