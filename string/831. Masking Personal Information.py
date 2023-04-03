class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            pass
            name, d_name = s.split("@")
            name = name.lower()
            d_name = d_name.lower()
            name = name[0]+"*****"+name[-1]
            return name+"@"+d_name
        else:
            new_s = ""
            for c in list(s):
                if c in ['+', '-', '(', ')', ' ']:
                    continue
                else:
                    new_s += c 

            local_num = new_s[-10:]
            # nation_num = s[:10]
            if len(new_s) == 10:
                return "***-***-{}".format(local_num[-4:])
            elif len(new_s) == 11:
                return "+*-***-***-{}".format(local_num[-4:]) 
            elif len(new_s) == 12:
                return "+**-***-***-{}".format(local_num[-4:])  
            else:
                return "+***-***-***-{}".format(local_num[-4:])  
            
if __name__ == "__main__":
    s = "86-(10)12345678"
    print(Solution().maskPII(s))