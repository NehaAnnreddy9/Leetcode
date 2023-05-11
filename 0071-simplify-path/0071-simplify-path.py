import collections
class Solution(object):
    def simplifyPath(self, path):
        st = collections.deque()
        dirs = path.split('/')
        dl = len(dirs)
        for i in range(dl):
            if dirs[i] == '': continue
            elif dirs[i] == '.': continue
            elif dirs[i] == '..':
                if len(st) > 0: st.pop()
            else: st.append(dirs[i])
        sl = len(st)
        if sl == 0: return "/"
        res = ''
        for i in range(sl): res = res + "/" + st[i]
        return res
                
        """
        :type path: str
        :rtype: str
        """
        