from typing import List
import itertools
import operator
from collections import defaultdict
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        
        for i in range(len(l)):
            left = l[i]
            right = r[i]
            sub_nums = nums[left:right+1]
            
            res.append(self.checkArithmetic(sub_nums))
        
        return res
        
    def checkArithmetic(self, nums):
        nums.sort()
        diff = nums[1] - nums[0]
        for i in range(1, len(nums)-1):
            if nums[i+1]-nums[i] != diff:
                return False
        return True

        
if __name__ == "__main__":
    nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
    l = [0,1,6,4,8,7]
    r = [4,4,9,7,9,10]
    
    print(Solution().checkArithmeticSubarrays(nums, l, r))

