class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        area = 0
        pos = [0,0]
        for i in range(len(heights)):
            while l < r:
                temp = min(heights[l],heights[r])*(r-l)
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
                if temp > area:
                    area = temp
                    pos = [l,r]
        return area