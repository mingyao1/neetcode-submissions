class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            mp[c].append(p)

        visited, cycle = set(), set()
        path = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)

            for p in mp[course]:
                if not dfs(p):
                    return False
            path.append(course)
            cycle.remove(course)
            visited.add(course)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return path 
