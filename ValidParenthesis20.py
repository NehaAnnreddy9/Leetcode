class Solution(object):
    def isValid(self, s):
        st = collections.deque()
        dict = {'[': ']','{':'}','(':')'}
        n = len(s)
        if n == 1: return False
        for i in range(n):
            if s[i] in dict.keys():
                st.append(s[i])
            else:
                if len(st) != 0 and dict[st[-1]] == s[i]:
                    st.pop()
                else: return False
        if len(st) == 0: return True
        else: return False
