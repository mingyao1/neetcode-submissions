class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                # append line
                spaces = (maxWidth - length) // max(1, (len(line) - 1))
                remainder = (maxWidth - length) % max(1, (len(line) - 1))
                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1

                res.append("".join(line))
                line, length = [], 0
            
            line.append(words[i])
            length += len(words[i])
            i += 1
        # last line
        for j in range(max(1, len(line) - 1)):
            line[j] += " "
        trail_spaces = maxWidth - (length + max(1, len(line) - 1))
        res.append("".join(line) + " " * trail_spaces)

        return res