class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] arr = new int[nums1.length];
        if(nums1.length == 0||nums2.length ==0)
            return arr;
        Arrays.fill(arr,-1);
        int flag=0;
        for(int i=0; i<nums1.length; i++)
        {
            for(int j=0;j<nums2.length;j++)
            {
                if(nums1[i]==nums2[j])
                {flag = 1;}  
                if(nums1[i]<nums2[j] && flag == 1)
                {arr[i] = nums2[j]; flag = 0; break;}  
            }
            if(arr[i] == -1){flag = 0;}
        }
        return arr;
    }
}