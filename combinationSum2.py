class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []

        def backtrack(curr, index, target):
            if target == 0:
                ans.append(curr[::])
                return 
            if target < 0:
                return 

            prev = -1
            for i in range(index, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtrack(curr, i + 1, target - candidates[i])
                curr.pop()
                prev = candidates[i]
            
        backtrack([], 0, target)
        return ans