def solution(id_list, report, k):
    report_count = {i: 0 for i in id_list}
    who_report_who = {i: [] for i in id_list}


    # # 신고 받은 횟수, 신고한 사람 init
    # for reporter_reported in (set(report)):
    #     reporter, reported = reporter_reported.split(" ")
    #     who_report_who[reporter].append(reported)
    #     report_count[reported] += 1

    print(report_count)
    print(who_report_who)

    # # k회 넘는 신고 받은 사람 찾기
    # sanctions = [key for key, val in report_count.items() if val >= k]
    # mail_count = {i: 0 for i in id_list}
    #
    # for sanction in sanctions:
    #     for reporter, reported in who_report_who.items():
    #         if sanction in reported:
    #             mail_count[reporter] += 1

    return []


if __name__ == '__main__':
    print(solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2)
    )  # [2, 1, 1, 0]
    print(solution(
        ["con", "ryan"],
        ["ryan con", "ryan con", "ryan con", "ryan con"],
        3)
    )  # [0,0]
