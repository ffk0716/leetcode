class Solution {
    public:
        int findLengthOfLCIS(const vector<int>& nums) {
            if (nums.size() <= 1)
                return nums.size();
            int max_c = 0;
            int c = 0;
            int pre_n = nums[0];                                                                                                           
            for (auto n : nums) {
                if (n > pre_n)
                    c++;
                else
                    c = 1;
                max_c = max(c, max_c);
                pre_n = n;
            }
            max_c = max(c, max_c);
            return max_c;
        }
};
