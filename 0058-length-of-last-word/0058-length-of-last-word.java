class Solution {
    public int lengthOfLastWord(String s) {
        int len = s.length();
        int length=0;
        if(len == 1)
            return 1;
        for(int i=len-1; i>-1;i--)
        {
            char c=s.charAt(i);
            if(c != ' ')
            {
                if(i == 0)
                {
                    length = 1;
                    break;
                }
                for(int j = i-1; j>-1;j--)
                {
                    char x = s.charAt(j);
                    if(x == ' ') 
                    {
                        length = i-j;
                        break;
                    }
                    else if(j == 0)
                    {
                        length = i+1;
                        break;
                    }
                }
            if(length>0)
            {
                break;
            }
                
            }
        }
        return length;
    }
}