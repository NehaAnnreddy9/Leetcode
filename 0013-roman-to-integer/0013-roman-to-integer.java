class Solution {
    public int romanToInt(String s) {
        int num = 0;
        int len = s.length();
        
        Map<Character, Integer> numMap = new HashMap<>();
        numMap.put('I',1);
        numMap.put('V',5);
        numMap.put('X',10);
        numMap.put('L',50);
        numMap.put('C',100);
        numMap.put('D',500);
        numMap.put('M',1000);
        num = num + numMap.get(s.charAt(len-1));
        
        for(int i=len-2; i>-1; i--)
        {
            int c = numMap.get(s.charAt(i));
            int c1 = numMap.get(s.charAt(i+1));
            if(c < c1)
            {
                num = num - c;
            }
            else
            { 
                num = num + c;
            }
        }
    return num;}
}