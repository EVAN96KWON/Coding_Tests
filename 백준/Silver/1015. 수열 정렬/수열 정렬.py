def spin_list(target, lst):
    target_index = lst.index(target)
    if target_index <= len(lst) - target_index:
        count = target_index
    else:
        count = len(lst) - target_index

    lst_spun = lst[target_index:] + lst[:target_index]

    return lst_spun, count


if __name__ == '__main__':
    N, M = map(int, input().split())
    targets = list(map(int, input().split()))

    count = 0
    my_list = [_ + 1 for _ in range(N)]

    for target in targets:
        while my_list[0] != target:
            my_list, add = spin_list(target, my_list)
            count += add
        else:
            del my_list[0]

    print(count)

