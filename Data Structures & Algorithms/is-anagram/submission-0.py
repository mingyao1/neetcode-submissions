class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len(sorted_s)):
            if not sorted_s[i] == sorted_t[i]:
                return False
        
        return True

