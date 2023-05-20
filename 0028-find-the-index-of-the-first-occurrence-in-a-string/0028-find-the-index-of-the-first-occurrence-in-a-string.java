class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.length()==0)
            return 0;
        //int ind = haystack.indexOf(needle);
        //return ind;
        int ind = -1;
        int len1=haystack.length();
        int len2=needle.length();
        if(haystack.equals(needle))
        {
            return 0;
        }
        for(int i=0; i<len1;i++)
        {
            char c = haystack.charAt(i);
            if(c == needle.charAt(0) && i+len2<=len1)
            {
                String subs = haystack.substring(i,i+len2); 
                if(needle.equals(subs))
                {
                    ind = i;
                    break;
                }
            }
        }
        return ind;
    }
}