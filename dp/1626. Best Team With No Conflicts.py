from typing import List
import itertools
import operator
from collections import defaultdict
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        status = sorted(zip(scores, ages))
        # status = sorted(status, key = lambda a: a[0])
        n = len(status)
        dp = [status[i][0] for i in range(n)]  # 默认值为自己单独组成一个队伍的socre
        
        for i, (score, age) in enumerate(status):
            for j in range(i):
                # 如果年龄符合要求
                if status[j][1] <= age:
                    dp[i] = max(dp[i], dp[j]+score)
        
        return max(dp)

        
if __name__ == "__main__":
    scores = [1,2,3,5]
    ages = [8,9,10,1]
    
    print(Solution().bestTeamScore(scores, ages))

