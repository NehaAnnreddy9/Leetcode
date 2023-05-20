
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        if(root == null) return list;
        
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        
        while(!stack.isEmpty()){
            TreeNode temp = stack.pop();
            list.add(0,temp.val);
            
            if(temp.left!= null) stack.push(temp.left);
            if(temp.right!= null) stack.push(temp.right);
        }
        return list;
    }
}