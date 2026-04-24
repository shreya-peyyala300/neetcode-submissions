class Solution {
    public boolean hasDuplicate(int[] nums) {
 Set<Integer> ui=new HashSet<>();
        for(int i=0;i<nums.length;i++){
            if(ui.contains(nums[i])){
            return true;}
            ui.add(nums[i]);
        }
        return false;
    }
}
