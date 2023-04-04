class Solution(object):
    def romanToInt(self, s):
        dict = {}
        dict['I'] = 1
        dict['V'] = 5
        dict['X'] = 10
        dict['L'] = 50
        dict['C'] = 100
        dict['D'] = 500
        dict['M'] = 1000
        n = len(s)
        rom = dict[s[0]]
        for i in range(1,n):
            if dict[s[i]] <= dict[s[i-1]]:
                rom = rom + dict[s[i]]
            else:
                rom = rom + dict[s[i]] - (2 * dict[s[i-1]])
        return rom

        """
        :type s: str
        :rtype: int
        """
