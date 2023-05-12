import itertools
class Solution(object):
    def letterCombinations(self, digits):
        if digits == '': return []
        dict = {
            "2" : ['a','b','c'], "3" : ['d','e','f'], "4" : ['g','h','i'], '5' : ['j','k','l'], '6' : ['m','n','o'], '7' : ['p','q','r','s'], '8' : ['t','u','v'], '9' : ['w','x','y','z']
        }
        lis = []
        for i in range(len(digits)): lis.append(dict[digits[i]])
        lis = list(itertools.product(*lis))
        ll = len(lis)
        for i in range(ll): lis[i] = ''.join(lis[i])
        return lis

        
        """
        :type digits: str
        :rtype: List[str]
        """
        