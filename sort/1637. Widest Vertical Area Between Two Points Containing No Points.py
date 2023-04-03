from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda a: a[0])
        max_diff = 0
        for i in range(len(points)):
            max_diff = max(max_diff, points[i][0]-points[i-1][0])
        
        return max_diff


if __name__ == "__main__":
    points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    print(Solution().maxWidthOfVerticalArea(points))