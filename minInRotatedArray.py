class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1

        lowest = float('inf')
        while(left < right):
            middle = (left + right) //2
            lowest = min(lowest, nums[middle])
            if(nums[middle] > nums[right]):
                left  = middle + 1
            else:
                right = middle -1 

        return min(lowest, nums[left])