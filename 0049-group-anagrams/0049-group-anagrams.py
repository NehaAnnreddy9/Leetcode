class Solution(object):
    
      def groupAnagrams(self, strs):
        ans = {}
        for s in strs: 
            x = tuple(sorted(s))
            if x in ans: ans[x].append(s)
            else: ans[x] = [s]
        return ans.values()
        
#     def groupAnagrams(self, strs): Brute force - O(m*n)
#         ans = []
#         hm = {}
        
#         for i in range(len(strs)):
#             thm = {}
#             for j in strs[i]:
#                 if j in thm: thm[j] += 1
#                 else: thm[j] = 1
#             hm[i] = thm
        
#         ans.append([0])
#         for i in range(1,len(strs)):
#             flg = 0
#             for j in range(0,len(ans)):
#                 if hm[ans[j][0]] == hm[i]: 
#                     ans[j].append(i)
#                     flg = 1
#             if flg == 0: ans.append([i])       
                    
                    
                    
#         for i in range(0, len(ans)):
#             for j in range(0, len(ans[i])):
#                 ans[i][j] = strs[ans[i][j]]
#         return ans
            
            
        
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        