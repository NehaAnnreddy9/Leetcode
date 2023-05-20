/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
            ListNode trav1 = list1;
            ListNode trav2 = list2;
            ListNode head = null;
            ListNode trav3 = null; 
            if(trav1 == null && trav2 == null)
            {
                return head;
            }
            else if(trav1 == null)
            {
                return list2;
            }
            else if(trav2 == null)
            {
                return list1;
            }
            if(trav1.val <= trav2.val)
            {
                head = new ListNode(trav1.val,null);
                trav3 = head;
                trav1 = trav1.next;
            }
            else if(trav1.val > trav2.val)
            {
                head =  new ListNode(trav2.val,null);
                trav3 = head;
                trav2 = trav2.next;
            }
            while(trav1 != null || trav2 != null)
            {
                if(trav1 == null)
                {
                    trav3.next = new ListNode(trav2.val,null);
                    trav3 = trav3.next;
                    trav2 = trav2.next;
                    continue;
                }
                else if(trav2 == null)
                {
                    trav3.next = new ListNode(trav1.val,null);
                    trav3 = trav3.next;
                    trav1 = trav1.next;
                    continue;
                    
                }
                if(trav1.val <= trav2.val)
                {
                    trav3.next = new ListNode(trav1.val,null);
                    trav3 = trav3.next;
                    trav1 = trav1.next;
                }
                else if(trav1.val > trav2.val)
                {
                    trav3.next = new ListNode(trav2.val,null);
                    trav3 = trav3.next;
                    trav2 = trav2.next;
                }
            }
           return head;
    }
}