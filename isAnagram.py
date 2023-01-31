import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = {}
        two = {}
        for i in s:
            if i not in one:
                one[i] = 1
            else:
                one[i] = one[i] + 1
        for i in t:
            if i not in two:
                two[i] = 1
            else:
                two[i] = two[i] + 1

        return True if one == two else False