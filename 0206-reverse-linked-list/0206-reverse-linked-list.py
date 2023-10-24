# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head != None:
            ptr1 = head
            ptr2 = head.next
            ptr = head
            while ptr2:
                ptr = ptr2.next
                ptr2.next = ptr1
                if ptr != None: 
                    ptr1 = ptr2
                    ptr2 = ptr
                else: 
                    head.next = None
                    head = ptr2
                    break
        return head
            
        """
        :type head: ListNode
        :rtype: ListNode
        """
        