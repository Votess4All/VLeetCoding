from typing import List
from functools import cache

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i + 1 == j:
                return 0
            return min(dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k] for k in range(i+1, j))
        
        return dfs(0, len(values)-1)
    

if __name__ == "__main__":
    values = [1,3,1,4,1,5]
    print(Solution().minScoreTriangulation(values))