class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        maxArea = 0

        while right > left:
            height = min(heights[right], heights[left])
            curArea = height * (right - left)
            maxArea = max(curArea, maxArea)

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        
        return maxArea
