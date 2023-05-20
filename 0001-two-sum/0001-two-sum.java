class Solution {
    public int[] twoSum(int[] nums, int target) {
        int array[] = new int[2];
        HashMap<Integer,Integer> numMap = new HashMap<Integer,Integer>();
        for (int i = 0; i < nums.length; i++) {
             int complement = target - nums[i];
             if (numMap.containsKey(complement)) {
                    array[0] = numMap.get(complement);
                    array[1] = i; 
                    return array;
            }
            numMap.put(nums[i],i);
        }
        return array;
    }
}