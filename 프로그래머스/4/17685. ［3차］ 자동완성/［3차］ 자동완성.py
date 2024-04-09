class Node(object):
    def __init__(self, key, cnt=0):
        self.key = key
        self.cnt = cnt
        self.child = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
            cur.cnt += 1

    def search(self, word):
        cur = self.head
        cnt = 0
        for c in word:
            cnt += 1
            cur = cur.child[c]
            if cur.cnt == 1:
                return cnt
        return len(word)


def solution(words):
    answer = 0
    trie = Trie()

    for word in words:
        trie.insert(word)

    for word in words:
        answer += trie.search(word)

    return answer
