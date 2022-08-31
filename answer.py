class Solution2(object):
    def isPalindrome(self, x):
        return False if x < 0 else str(x)[::-1] == str(x)
