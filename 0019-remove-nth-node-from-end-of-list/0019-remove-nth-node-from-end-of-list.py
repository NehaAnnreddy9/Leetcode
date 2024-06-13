# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        f, s = head, head
        head = d
        
        while n and s:
            s = s.next
            n -= 1
            
        while s:
            d = d.next
            f = f.next
            s = s.next
                    
        d.next = d.next.next
        return head.next