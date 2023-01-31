class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        earilestEnd = float('-inf')
        ans = 0
        for start, end in sorted(intervals, key=lambda x:x[1]):
            if(start >= earilestEnd):
                earilestEnd = end
            else:
                ans += 1
            
        return ans