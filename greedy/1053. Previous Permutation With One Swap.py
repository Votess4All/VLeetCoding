from typing import List 

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-2, -1, -1):
            # 从右往左找，找到靠右的可能构成小于原数字的数
            if arr[i+1] < arr[i]:
                for j in range(n-1, i, -1):
                    # 从右往左找，找到靠右的符合无限接近的要求，如果有重复的数字，则直接跳过
                    if arr[j] != arr[j-1] and arr[j] < arr[i]:
                        arr[j], arr[i] = arr[i], arr[j]
                        return arr
        
        return arr

if __name__ == "__main__":
    arr = [1,9,4,6,7]
    print(Solution().prevPermOpt1(arr))