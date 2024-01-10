class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = vowels = len([c for c in s[:k] if c in "aeiou"])
        for i in range(k, len(s)):
            if s[i - k] in "aeiou":
                vowels -= 1
            if s[i] in "aeiou":
                vowels += 1
            max_vowels = max(max_vowels, vowels)
        return max_vowels
