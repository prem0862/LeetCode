

class Solution:
    def trailingZeroes(self, n: int) -> int:
        number = n
        trailing_zeros = 0
        divisor = 5
        while number > 0:
            number = math.floor(number/divisor)
            trailing_zeros += number
        return trailing_zeros


        

"""
	Problem Link: https://leetcode.com/problems/factorial-trailing-zeroes/
"""