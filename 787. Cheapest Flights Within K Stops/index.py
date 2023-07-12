from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [[float('inf')] * n for _ in range(k+2)]

        for i in range(k+2):
            dp[i][src] = 0

        for i in range(1, k+2):
            for u, v, w in flights:
                if dp[i-1][u] != float('inf'):
                    dp[i][v] = min(dp[i][v], dp[i-1][u] + w)

        if dp[k+1][dst] == float('inf'):
            return -1
        else:
            return dp[k+1][dst]
