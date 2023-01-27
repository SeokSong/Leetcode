class Solution:
    def findGCD(self, nums: List[int]) -> int:
        lowest = float('inf')
        highest = float('-inf')

        for i in nums:
            if(lowest > i):
                lowest = i
            if(highest < i):
                highest = i
        for i in range(lowest, 0, -1):
            if(highest % i == 0 and lowest % i == 0):
                print("done")
                return i
        return 1