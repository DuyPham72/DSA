class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        result = []
        courses = [0]*numCourses
        def dfs(i):
            node = courses[i]
            if node == 1:
                return False
            if node == 2:
                return True

            courses[i] = 1
            for nei in g[i]:
                if not dfs(nei):
                    return False

            courses[i] = 2
            result.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return result