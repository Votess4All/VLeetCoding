from functools import lru_cache

class Solution:
    def countVowelStrings(self, n: int) -> int:
        @lru_cache
        def dfs(i, j):
            if i >= n:
                return 1
            
            return sum(dfs(i+1, k) for k in range(j, 5))
        
        return dfs(0, 0)


if __name__ == "__main__":
    n = 33
    print(Solution().countVowelStrings(n))