class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            mp[c].append(p)
        
        res = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for p in mp[course]:
                if dfs(p) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return res
