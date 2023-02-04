class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1: 
            return 1
        
        left, right = 0, n

        while(left < right):
            middle = (right + left)//2
            leftHalf = 0
            rightHalf = 0
            for i in range(middle + 1):
                leftHalf += i
            for i in range(middle, n + 1):
                rightHalf += i
            if(leftHalf == rightHalf):
                return middle
            if(leftHalf > rightHalf):
                right = middle -1
            else:
                left = middle + 1
        return -1