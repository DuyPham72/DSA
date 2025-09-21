class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        max_len = max(len(x) for x in wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(1, min(i, max_len) + 1):
                if not dp[i - j]:
                    continue
                if s[i - j:i] in wordset:
                    dp[i] = True
                    break

        return dp[-1]