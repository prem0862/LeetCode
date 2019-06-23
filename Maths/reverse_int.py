


import math

class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False if x > 0 else True
        str_num = str(abs(x))
        rev_num = ""
        for i in range(len(str_num) -1, -1, -1):
            rev_num += str_num[i]
            
        rev_num = int(rev_num)
        if is_negative:
            rev_num = (-1)*(rev_num)
            
        if rev_num > (math.pow(2, 31) -1) or rev_num < (-1*math.pow(2, 31)):
            rev_num = 0
            
        return rev_num





"""
	Problem Link: https://leetcode.com/problems/reverse-integer/
"""