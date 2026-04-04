class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            mp[c].append(p)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if mp[course] == []:
                return True
            
            visited.add(course)

            for p in mp[course]:
                if not dfs(p):
                    return False
            
            mp[course] = []
            visited.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            

            

        
