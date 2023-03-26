from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        vis = set()
        for i in range(len(nums)-1):
            _sum = nums[i] + nums[i+1]
            if _sum in vis:
                return True
            vis.add(_sum)
        
        return False

if __name__ == "__main__":
    nums = [4,2,4]
    print(Solution().findSubarrays(nums))