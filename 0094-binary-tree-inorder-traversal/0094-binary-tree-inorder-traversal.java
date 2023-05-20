
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
         List<Integer> list = new ArrayList<Integer>(); 
            if(root == null)
                return list;
            Stack<TreeNode> stack = new Stack<TreeNode>();           
            TreeNode trav = root;
            while(trav!= null || !stack.isEmpty()){
                while(trav!= null)
                {
                    stack.push(trav);
                    trav = trav.left;
                }
                
                trav = stack.pop();
                list.add(trav.val);
                trav = trav.right;
            }
                    
           return list;
        
           
    }
}