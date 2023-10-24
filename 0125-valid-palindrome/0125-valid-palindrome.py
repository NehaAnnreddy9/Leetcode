class Solution(object):
    def isPalindrome(self, s):
        s = "".join([x for x in s.lower() if x.isalnum()])
        return s == s[::-1]
        """
        :type s: str
        :rtype: bool
        """
        