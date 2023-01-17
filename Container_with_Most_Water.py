class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) -1
        while(left < right):
            area = min(height[left], height[right]) * (right - left)
            water = max(water, area)
            if(height[left] < height[right]):
                left += 1
            elif(height[left] >= height[right]):
                right -= 1
        return water
