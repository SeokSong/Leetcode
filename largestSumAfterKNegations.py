class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        changes = 0

        for i in range(len(nums)):
            if(nums[i] < 0 and changes < k):
                nums[i] *= -1
                changes += 1

        while((k - changes) >= 2):
            changes += 2 

        nums = sorted(nums)
        
        if((k - changes) >= 1): #we can only 
            changes += 1 
            nums[0] *= -1

        return sum(nums)
        