def make_edge(party_members):
    for person in party_members:
        others = party_members - {person}
        for other in others:
            graph[person].add(other)
            graph[other].add(person)


def tell_truth(person):
    if heard_truth[person]:
        return

    heard_truth[person] = True

    for next_person in graph[person]:
        tell_truth(next_person)


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = {n: set() for n in range(1, N + 1)}
    parties = []
    knows_truth = [False] + [False] * N
    heard_truth = [False] + [False] * N

    input_2 = input()
    if input_2 != '0':
        for i in list(map(int, input_2[2:].split())):
            knows_truth[i] = True
        for m in range(M):
            party = set(list(map(int, input().split()))[1:])
            parties.append(party)
            make_edge(party)

    for i in range(len(knows_truth)):
        if knows_truth[i]:
            tell_truth(i)

    for party in parties:
        for person in party:
            if heard_truth[person]:
                M -= 1
                break

    print(M)
