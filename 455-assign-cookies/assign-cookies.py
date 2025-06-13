class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        kids, cookies = sorted(g), sorted(s)

        kid_idx = 0
        for cookie in cookies:
            if kid_idx < len(kids) and cookie >= kids[kid_idx]:
                kid_idx += 1
                
        return kid_idx