class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        last = 0
        for i in range(len(s)):
            for j in range(last, len(t)):
                if s[i] == t[j]:
                    last = j + 1
                    break
            else:
                return False
        return True

