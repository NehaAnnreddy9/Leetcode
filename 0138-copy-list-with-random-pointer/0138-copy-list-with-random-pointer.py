"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None: return head
        
        curr = head
        hm = {}
        i = 0
        while curr != None:
            hm[curr] = i
            curr = curr.next
            i = i + 1
            
        hm[None] = i
        last = i
            
        arr2 = []
        curr = head
        while curr != None:
            arr2.append(hm[curr.random])
            curr = curr.next

        
        arr = []
        head1 = Node(head.val, None, None)
        st = head1
        arr.append(st)
        curr = head.next
        while curr != None:
            st.next = Node(curr.val, None, None)
            st = st.next
            arr.append(st)
            curr = curr.next
        
        st = head1
        for i in arr2:
            if i != last: st.random = arr[i]
            else:  st.random = None
            st = st.next
            
        return head1
            
            
        