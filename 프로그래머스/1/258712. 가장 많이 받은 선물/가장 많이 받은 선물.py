from itertools import combinations


def solution(friends, gifts):
    indexs = {f: i for i, f in enumerate(friends)}
    scores = {f: 0 for f in friends}

    # init adj mat give_n_take
    give_n_take = [[0] * len(friends) for _ in range(len(friends))]
    for gift in gifts:
        f, t = gift.split(" ")
        give_n_take[indexs[f]][indexs[t]] += 1

    # init scores
    for friend in friends:
        given = sum(give_n_take[indexs[friend]])
        taken = sum([i[indexs[friend]] for i in give_n_take])
        scores[friend] = given - taken

    # calc bonus
    bonus = [0] * len(friends)
    for p1, p2 in combinations(friends, 2):
        p1_to_p2 = give_n_take[indexs[p1]][indexs[p2]]
        p2_to_p1 = give_n_take[indexs[p2]][indexs[p1]]

        if p1_to_p2 > p2_to_p1:
            bonus[indexs[p1]] += 1
        elif p1_to_p2 < p2_to_p1:
            bonus[indexs[p2]] += 1
        else:
            if scores[p1] > scores[p2]:
                bonus[indexs[p1]] += 1
            elif scores[p1] < scores[p2]:
                bonus[indexs[p2]] += 1

    return max(bonus)
