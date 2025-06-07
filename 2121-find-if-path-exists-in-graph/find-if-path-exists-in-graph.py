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
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei_node in dic[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stack.append(nei_node)

        return False