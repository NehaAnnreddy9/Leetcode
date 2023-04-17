class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None and list2 == None: return None
        elif list1 == None: return list2
        elif list2 == None: return list1 
        head = ListNode()
        pt = head
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                pt.next = ListNode(list1.val)
                pt = pt.next
                list1 = list1.next
            else:
                pt.next = ListNode(list2.val)
                pt = pt.next
                list2 = list2.next
        if list1 == None: pt.next = list2 
        elif list2 == None: pt.next = list1 
        pt = head.next
        return pt
