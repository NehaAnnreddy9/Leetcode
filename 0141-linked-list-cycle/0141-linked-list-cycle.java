/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode trav = head;
        HashMap<ListNode,Integer> hash_map = new HashMap<ListNode,Integer>();
        if(head == null || head.next == null)
        {
            return false;
        }
        hash_map.put(trav,trav.val);
        trav = trav.next;
        while(hash_map.containsKey(trav) != true)
        {
            hash_map.put(trav,trav.val);
            trav = trav.next;
            if(trav == null)
                break;
        }
        if(trav != null)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}