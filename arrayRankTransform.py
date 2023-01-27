class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = []
        track = {}

        nums = sorted(arr)
        
        index = 0
        for i, num in enumerate(nums):
            if(num not in track):
                track[num] = index
                index += 1

        for index, num in enumerate(arr):
            ans.append(track[num] + 1)
        
        return ans
            