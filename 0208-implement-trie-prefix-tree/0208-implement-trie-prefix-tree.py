class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cn = self.root
        for c in word:
            if c not in cn.children: cn.children[c] = TrieNode()
            cn = cn.children[c]
        cn.is_end_of_word = True
        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        cn = self.root
        if len(cn.children) != 0:
            for c in word:
                if c not in cn.children: return False
                cn = cn.children[c]
            if cn.is_end_of_word == True: return True    
        return False
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        cn = self.root
        if len(cn.children) != 0:
            for c in prefix:
                if c not in cn.children: return False
                cn = cn.children[c]
            return True
        return False
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)