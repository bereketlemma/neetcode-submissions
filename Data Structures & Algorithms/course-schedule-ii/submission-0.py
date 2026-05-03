class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisites_map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prerequisites_map[course].append(pre)

        output = []
        visit = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for pre in prerequisites_map[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True 
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output







