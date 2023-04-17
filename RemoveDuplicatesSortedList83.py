class Solution(object):
    def deleteDuplicates(self, head):
        if head == None: return None
        if head.next == None: return head
        pt = head
        st = None
        while pt.next != None:
            if st == None and pt.val == pt.next.val:
                st = pt
            elif st != None and pt.val != pt.next.val:
                st.next = pt.next
                st = None
            pt = pt.next
        if st != None: st.next = None
        return head
