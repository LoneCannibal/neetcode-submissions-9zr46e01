class Solution {
    public int[] sortArray(int[] nums) {
        for(int i=0; i<nums.length; i++) {
            int min =i;
            for(int j=i; j<nums.length; j++) {
                if(nums[min] > nums[j])
                    min = j;
            }
            int temp = nums[min];
            nums[min] = nums[i];
            nums[i] = temp;
        }
        return nums;
    }
}