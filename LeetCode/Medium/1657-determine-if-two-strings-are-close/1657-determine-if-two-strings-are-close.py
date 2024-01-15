class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        return set(word1) == set(word2) and sorted(c1.values()) == sorted(c2.values())
