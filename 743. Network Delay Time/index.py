from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf')] * n
        distances[k-1] = 0

        for _ in range(n-1):
            for u, v, w in times:
                if distances[u-1] + w < distances[v-1]:
                    distances[v-1] = distances[u-1] + w

        for u, v, w in times:
            if distances[u-1] + w < distances[v-1]:
                return -1

        max_time = max(distances)
        return max_time if max_time != float('inf') else -1