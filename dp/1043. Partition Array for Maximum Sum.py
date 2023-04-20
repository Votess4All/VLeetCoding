class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0 for _ in range(n)]
        for i in range(k):
            dp[i] = max(arr[:i+1]) * (i+1)
        # print(dp)
        for i in range(k, n):
            for j in range(1, k+1):
                # j 代表最后一个分割数组的长度
                # print(i-j, i-j+1, i+1)
                dp[i] = max(dp[i], dp[i-j] + max(arr[i-j+1:i+1]) * j)
        # print(dp)
        return dp[-1]
    

if __name__ == "__main__":
    arr = [1,4,1,5,7,3,6,1,9,9,3]
    k = 4   
    print(Solution().maxSumAfterPartitioning(arr, k))