class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        courses = [0]*numCourses
        def dfs(i):
            node = courses[i]
            if node == 1: return False
            if node == 2: return True

            courses[i] = 1
            for neighbor in g[i]:
                if not dfs(neighbor):
                    return False

            courses[i] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True