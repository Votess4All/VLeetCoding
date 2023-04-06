class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = "0"*(len(b)-len(a)) + a
        else:
            b = "0"*(len(a)-len(b)) + b

        n = len(a)-1
        remain = 0
        result = ""
        while n >= 0:
            _a = int(a[n])
            _b = int(b[n])

            res = (_a+_b+remain) % 2
            remain = (_a+_b+remain) // 2
            
            result += "{}".format(res)
            n -= 1
        
        if remain:
            result += "{}".format(remain)
        
        return result[::-1]
    
if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(Solution().addBinary(a, b))