class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b)

        course = [0] * numCourses
        result = []
        def dfs(i):
            node = course[i]
            if node == 1: return False
            if node == 2: return True

            course[i] = 1
            for neighbor in g[i]:
                if not dfs(neighbor):
                    return False

            course[i] = 2
            result.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return result