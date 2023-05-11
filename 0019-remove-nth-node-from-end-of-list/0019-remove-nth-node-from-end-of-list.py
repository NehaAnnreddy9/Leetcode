# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fptr = head
        sptr = head
        for i in range(n): fptr = fptr.next
        if fptr == None: return head.next
        while fptr.next != None:
            fptr = fptr.next
            sptr = sptr.next
        sptr.next = sptr.next.next
        return head
        
        
                 
            
                
                
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        