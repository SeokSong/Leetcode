class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []


        def backtracking(index, prev, subset):
            if(prev == target):
                ans.append(subset.copy())
                return
            if(index >= len(candidates) or prev > target):
                    return 

            subset.append(candidates[index])
            backtracking(index, prev + candidates[index], subset)
            subset.pop()
            backtracking(index + 1, prev, subset)                

        backtracking(0, 0, [])

        return ans