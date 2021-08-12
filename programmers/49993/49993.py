def check_my_tree(my_tree, skill):
    for k in range(len(my_tree)):
        if my_tree[k] != skill[k]:
            return False
    return True


def solution(skill, skill_trees):
    answer = 0

    skill = list(skill)
    for i in range(len(skill_trees)):
        skill_trees[i] = list(skill_trees[i])
        tmp = []
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                tmp.append(skill_trees[i][j])

        answer += 1 if check_my_tree(tmp, skill) else 0

    return answer


if __name__ == '__main__':
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
