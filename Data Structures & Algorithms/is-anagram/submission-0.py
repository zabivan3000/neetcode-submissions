class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            return sorted(s) == sorted(t)