class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxTillNow = float('-inf')
        maxEnding = 0
        
        for i in range(0, len(nums)):
            maxEnding = max(nums[i], maxEnding + nums[i])
            maxTillNow =max(maxEnding, maxTillNow)

        return maxTillNow