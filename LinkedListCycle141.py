class Solution(object):
    def hasCycle(self, head):
        fp = head
        sp = head
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
            if fp == sp: return True
        return False
