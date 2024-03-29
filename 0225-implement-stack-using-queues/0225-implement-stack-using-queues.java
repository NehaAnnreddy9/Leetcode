class MyStack {
    Queue<Integer> q;

    public MyStack() {
        q = new LinkedList<>();
    }
    
    public void push(int x) {
       int n = q.size();
       q.add(x); 
       while(n-->0)
           q.add(q.remove());
    }
    
    public int pop() {
            return q.remove();       
    }
    
    public int top() {
        return q.peek() ;
    }
    
    public boolean empty() {
        if(q.size() == 0)
            return true;
        else
            return false;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */