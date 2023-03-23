from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # 代表以nums[i]结尾的最长递增子序列的长度，默认为1

        for i in range(1, n):
            for j in range(i):
                # 只有当nums[i]比nums[j]大的时候，dp[i]代表的最长递增子序列的长度才会得到更新
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums))