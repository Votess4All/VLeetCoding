from typing import List
import itertools
import operator
from collections import defaultdict
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        # 缩小问题规模，初始化 right = n-1，right左移知道找到第一个位置使得arr[right:n-1]不满足非递减
        right = n - 1
        while right > 0 and arr[right-1] <= arr[right]:
            right -= 1
            
        # 说明整个数组都满足非递减
        if right == 0:
            return 0
        
        left = 0
        ans = right
        # 为了保证剩余子数组非递减，枚举left直到对于当前right，有arr[left] <= arr[right]
        while left == 0 or arr[left-1] <= arr[left]:
            while right < n and arr[left] > arr[right]:
                right += 1
            
            ans = min(ans, right-left-1)
            left += 1
        
        return ans

        
if __name__ == "__main__":
    arr = [6,3,10,11,15,20,13,3,18,12]
    
    print(Solution().findLengthOfShortestSubarray(arr))

