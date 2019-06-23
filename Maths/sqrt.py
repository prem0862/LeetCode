

class Solution:
    def mySqrt(self, A:int) -> int:
        high = A
        low = 1
        while high >= low:
            mid = int((low + high) / 2)
            # Check if mid = floor(sqrt(A))
            if  mid*mid <= A and (mid+1)*(mid+1) > A:
                return mid
            elif mid*mid < A:
                low = mid + 1
            else:
                high = mid - 1
        
        return 0 # If we were given 0, return 0 (this is the only way we'll get here


        
        
"""
	Problem Link: https://leetcode.com/problems/sqrtx/
"""