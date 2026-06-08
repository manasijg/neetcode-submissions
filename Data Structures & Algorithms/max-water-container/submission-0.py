class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0
        i , j = 0, len(heights)-1

        while i < j:
            area = (min(heights[i], heights[j]) * (j-i))
            maxW = max(maxW, area)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
    
        return maxW
             