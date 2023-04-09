from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        visited = set()
        n = len(s)
        
        for cur_pos, char in enumerate(s):
            
            if not char in visited:
                visited.add(char)
            else:
                continue
            
            end = cur_pos + distance[ord(char) - ord("a")]+1
            if end < n and s[end] == char:
                continue
            else:
                return False
        
        return True
    
if __name__ == "__main__":
    s = "aa"
    distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    print(Solution().checkDistances(s, distance))