if __name__ == '__main__':
    q = int(input())
    company = dict()
    count = 0

    for _ in range(q):
        s, p = list(map(str, input().split()))

        if p == '-':
            if s not in company or company[s] == 0:
                count += 1
            elif s in company:
                company[s] -= 1
        else:
            if s not in company:
                company[s] = 1
            else:
                company[s] += 1

    if len(company) == 0:
        print(count)
    else:
        print(sum(company.values()) + count)

