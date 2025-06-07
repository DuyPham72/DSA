class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        dic = defaultdict(list)
        for start, end in edges:
            dic[start].append(end)
            dic[end].append(start)

        seen = set()
        seen.add(source)

        def dfs(node):
            if node == destination:
                return True

            for neighbor in dic[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True

            return False

        return dfs(source)