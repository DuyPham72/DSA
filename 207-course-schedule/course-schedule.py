class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for start, end in prerequisites:
            graph[start].append(end)

        in_course = [0] * numCourses
        def dfs(i):
            node = in_course[i]
            if node == 1:
                return False
            if node == 2:
                return True

            in_course[i] = 1
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    return False

            in_course[i] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True