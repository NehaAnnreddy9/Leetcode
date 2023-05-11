# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None: return head
        p = head
        n = head.next
        adr = n.next
        n.next = p
        p.next = adr
        head = n
        pr = p
        p = p.next
        if p != None: 
            n = p.next
            while n != None:
                adr = n.next
                n.next = p
                p.next = adr
                pr.next = n
                pr = p
                p = p.next
                if p == None: break
                n = p.next
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        