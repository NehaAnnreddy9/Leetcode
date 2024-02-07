class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        
class WordDictionary:

    def __init__(self):
         self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cn = self.root
        for c in word:
            if c not in cn.children: cn.children[c] = TrieNode()
            cn = cn.children[c]
        cn.is_end_of_word = True
        

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cn = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.': 
                    for child in cn.children.values():
                        if dfs(i+1, child) == True: return True
                    return False
                elif c not in cn.children: return False
                else: cn = cn.children[c]
            return cn.is_end_of_word 
        
        return dfs(0, self.root)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)