class Solution {
    public boolean isValid(String s) {
        int len = s.length();
        boolean valid = true;
        char topc = ' ';
        Stack<Character> stack = new Stack<Character>();
        if(len==1)
        { 
            valid = false;
            return valid;
        }
        for(int i=0;i<len;i++)
        { 
            if(stack.empty())
                topc = ' ';
            else
                topc = stack.peek();
            char c = s.charAt(i);
           if((c == ')' && topc =='(') || (c == '}' && topc =='{') || (c == ']' && topc =='['))
                stack.pop();
            else
                stack.push(c);
        }
        
        if(stack.empty())
        {
            valid = true; 
        }
        else
        {
            valid = false;
        }
        return valid;
    }
}