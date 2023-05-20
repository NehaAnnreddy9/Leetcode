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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode trav = head;
        ListNode temp = null;
        ListNode trav2 = null;
        if(head == null)
            return head;
        while(trav.next != null)
        {
            temp = trav.next;
            if(trav.val == trav.next.val)
            {
                trav2 = trav.next;
                while(trav2.val == trav.val)
                {
                    if(trav2.next == null)
                    {
                        trav2 =  null;
                        break;
                    }
                    else
                    {trav2 = trav2.next;}   
                }
                
                trav.next = trav2;
                temp = null;
                if(trav2 == null)
                {
                    return head;
                }
                trav = trav.next;   
            }
            else
            {
                trav = trav.next;
            }
        }
        return head;
    }
}