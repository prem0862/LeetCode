

class Solution:
    def isPalindrome(self, x: int) -> bool:
        is_palindrome = True
        string_param = str(x)
        len_param = len(string_param)
        for i in range(0, len_param):
            if string_param[i] != string_param[len_param -1 -i]:
                is_palindrome = False
                break
        return is_palindrome



 """
	Problem Link: https://leetcode.com/problems/palindrome-number/
 """