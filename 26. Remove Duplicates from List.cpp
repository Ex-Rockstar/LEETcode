class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int p2=1;
        for(int p1 =1;p1<nums.size();p1++){
            if(nums[p1] != nums[p1-1]){
                nums[p2]=nums[p1];
                p2++;
            }
        }
        return p2;
        
    }
};