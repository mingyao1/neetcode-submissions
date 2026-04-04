class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ";" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0

        while index < len(s):
            i = index
            while not s[i] == ";":
                i += 1
            length = int(s[index:i])
            res.append(s[i + 1: i + 1 + length])
            index = i + 1 + length

        return res