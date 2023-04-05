class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        _min = min(a, b)
        res = 0
        for i in range(1, _min+1):
            if a % i == 0 and b % i == 0:
                res += 1
        
        return res
    

if __name__ == "__main__":
    a = 25
    b = 30
    
    print(Solution().commonFactors(a, b))

