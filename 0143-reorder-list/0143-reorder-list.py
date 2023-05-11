# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import collections
class Solution(object):
    def reorderList(self, head):
        st = collections.deque()
        p1 = head
        while p1 != None:
            st.append(p1)
            p1 = p1.next
        p1 = head
        p2 = st.pop()
        while p1 != p2 and p1.next != p2:
            addr = p1.next
            p1.next = p2
            p2.next = addr
            p1 = p2.next
            p2 = st.pop()
            p2.next = None
            if p1 == st[-1]: break
        return head
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        