

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True
        
        self_div_nums = []
        for n in range(left, right + 1):
            if self_dividing(n):
                self_div_nums.append(n)
                
        return self_div_nums


"""
	Problem Link: https://leetcode.com/problems/self-dividing-numbers/
"""