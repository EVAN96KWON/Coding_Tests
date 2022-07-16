def to_sec(HMS: str):
    h, m, s = map(int, HMS.split(":"))
    return h * 60 * 60 + m * 60 + s


def to_hms(s: int):
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return "{0:0>2}:{1:0>2}:{2:0>2}".format(h, m, s)


def solution(play_time, adv_time, logs):
    answer = ''
    play_time = to_sec(play_time)
    adv_time = to_sec(adv_time)

    timeline = [0] * (play_time + 1)

    for log in logs:
        start, end = map(to_sec, log.split('-'))
        for i in range(start, end + 1):
            timeline[i] += 1

    max_view = 0
    max_time = 0

    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if max_view < timeline[i] - timeline[i - adv_time]:
                max_view = timeline[i] - timeline[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if max_view < timeline[i]:
                max_view = timeline[i]
                max_time = i - adv_time + 1

    return max_time


if __name__ == '__main__':
    print(solution("02:03:55", "00:14:15",
                   ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                    "01:37:44-02:02:30"]))  # "01:30:59"
    print(solution("99:59:59", "25:00:00",
                   ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))  # "01:00:00"
    print(solution("50:00:00", "50:00:00",
                   ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))  # "00:00:00"
