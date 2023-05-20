class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        int len = strs.length;
        String first = strs[0];
        String last = strs[len-1];
        String pf = "";
        int flag = 0;
        if(first.length() < last.length()){ len = first.length();}
        else{ len = last.length();}
        for(int i=0; i<len; i++)
        {
            if(first.charAt(i) == last.charAt(i) && flag == i)
            {
                pf = pf + first.charAt(i);
                flag = flag+1;
            }
        }
        if(pf.length() == 0)
            return "";
        else
            return pf;
    }
}