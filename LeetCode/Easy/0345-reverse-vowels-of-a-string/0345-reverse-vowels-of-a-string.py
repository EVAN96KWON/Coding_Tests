class Solution:
    def reverseVowels(self, s: str) -> str:
        gathers = [c for c in s if c.lower() in "aeiou"]
        ret = [c if c.lower() not in "aeiou" else gathers.pop() for c in s]
        return "".join(ret)