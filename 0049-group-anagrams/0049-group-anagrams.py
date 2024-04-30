class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li, hmp = [], defaultdict(list)
        for i in range(len(strs)):
            hmp[tuple(sorted(strs[i]))].append(i)
            
        for i, v in hmp.items():
            l = []
            for j in v:
                l.append(strs[j])
            li.append(l)
            
        return li
            
        