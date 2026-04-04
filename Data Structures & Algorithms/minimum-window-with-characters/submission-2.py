class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        window = {}
        res = [-1, -1]
        minLen = float('inf')
        l = 0

        have, need = 0, len(count)
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in count and count[s[r]] == window[s[r]]:
                have += 1

                while have == need:
                    if r - l + 1 < minLen:
                        minLen = r - l + 1
                        res = [l, r + 1]
                        
                    window[s[l]] -= 1
                    if s[l] in count and window[s[l]] < count[s[l]]:
                        have -= 1
                    l += 1
        
        return s[res[0]: res[1]] if minLen != float('inf') else ""

