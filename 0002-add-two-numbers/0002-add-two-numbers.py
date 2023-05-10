# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        p = head
        prev = head
        co = 0
        while l1 != None and l2 != None:
            val = l1.val + l2.val + co
            if val >= 10:
                p.val = val % 10
                co = 1
            else: 
                p.val = val
                co = 0
            l1 = l1.next
            l2 = l2.next
            prev = p
            p.next = ListNode()
            p = p.next

        l = l1 if l1 != None else l2
        if l != None:
            while l != None:
                val = l.val + co
                if val >= 10:
                    p.val = val % 10
                    co = 1
                else: 
                    p.val = val
                    co = 0
                l = l.next
                prev = p
                p.next = ListNode()
                p = p.next
        
        if co == 1: p.val = 1
        else: prev.next = None 
        return head
            

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """