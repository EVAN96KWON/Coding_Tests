def solution(s):
    answer = ""
    words = s.lower().split(" ")

    for word in words:
        answer += word.capitalize() + " " if word else ' '

    return answer[:-1]


if __name__ == '__main__':
    print(solution("3people  unFollowed me"))  # "3people Unfollowed Me"
    print(solution("for the last week"))  # "For The Last Week"
