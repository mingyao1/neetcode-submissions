class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque()
        visited = set(deadends)
        q.append((("0000"), 0))

        def getChildren(lock):
            res = []
            for i in range(4):
                x = int(lock[i])
                x1 = (x - 1 + 10) % 10
                x2 = (x + 1) % 10
                res.append(lock[:i] + str(x1) + lock[i + 1:])
                res.append(lock[:i] + str(x2) + lock[i + 1:])
            return res

        while q:
            lock, turn = q.popleft()
            if lock == target:
                return turn
            print(lock)
            children = getChildren(lock)
            for c in children:
                if c not in visited:
                    visited.add(c)
                    q.append((c, turn + 1))
        
        return -1