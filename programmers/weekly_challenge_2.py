def get_student_avg(student_num, scores):
    student_score = []
    max = 0
    min = 100
    deleted = 0

    for i in range(len(scores)):
        if max < scores[i][student_num]:
            max = scores[i][student_num]
        if min > scores[i][student_num]:
            min = scores[i][student_num]
        student_score.append(scores[i][student_num])

    if max == student_score[student_num] or min == student_score[student_num]:
        deleted = student_score.pop(student_num)

    if deleted in student_score:
        student_score.append(deleted)

    return sum(student_score) / len(student_score)


def solution(scores):
    answer = ''

    for student_num in range(len(scores)):
        score = get_student_avg(student_num, scores)
        if score >= 90:
            answer += 'A'
        elif 80 <= score < 90:
            answer += 'B'
        elif 70 <= score < 80:
            answer += 'C'
        elif 50 <= score < 70:
            answer += 'D'
        else:
            answer += 'F'

    return answer


if __name__ == '__main__':
    print(solution([[100, 90, 98, 88, 65],
                    [50, 45, 99, 85, 77],
                    [47, 88, 95, 80, 67],
                    [61, 57, 100, 80, 65],
                    [24, 90, 94, 75, 65]]))
    # "FBABD"
    print(solution([[50, 90],
                    [50, 87]]))
    # "DA"
    print(solution([[70, 49, 90],
                    [68, 50, 38],
                    [73, 31, 100]]))
    # "CFD"
    print(solution([[75, 50, 100],
                    [75, 100, 20],
                    [100, 100, 20]]))
    # "BBF"
