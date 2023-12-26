def find_cheapest(brand_list):
    set_list = list()
    cheapest_one = 1000

    for brand in brand_list:
        if cheapest_one >= brand[1]:
            cheapest_one = brand[1]
        set_list.append(min(brand[0], brand[1] * 6))

    return min(set_list), cheapest_one


if __name__ == '__main__':
    N, M = map(int, input().split())
    brand_list = [list(map(int, input().split())) for _ in range(M)]
    cheapest_set, cheapest_one = find_cheapest(brand_list)
    answer = 0

    while N > 6:
        answer += cheapest_set
        N -= 6
    else:
        if cheapest_set <= cheapest_one * N:
            answer += cheapest_set
        else:
            answer += N * cheapest_one

    print(answer)
