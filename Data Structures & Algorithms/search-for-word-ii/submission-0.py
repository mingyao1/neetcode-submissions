class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        M, N = len(board), len(board[0])
        root = TrieNode()
        for w in words:
            root.addWord(w)
        visited, res = set(), set()

        def dfs(m, n, node, s):
            if m < 0 or m >= M or n < 0 or n >= N or ((m, n) in visited) or board[m][n] not in node.children:
                return

            node = node.children[board[m][n]]
            s += board[m][n]
            if node.isWord: 
                res.add(s)
     
            visited.add((m, n))
            dfs(m + 1, n, node, s)
            dfs(m - 1, n, node, s)
            dfs(m, n + 1, node, s)
            dfs(m, n - 1, node, s)
            visited.remove((m, n))
        
        for i in range(M):
            for j in range(N):
                dfs(i, j, root, "")
        
        return list(res)


