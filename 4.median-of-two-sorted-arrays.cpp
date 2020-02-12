/*
 * @lc app=leetcode id=4 lang=cpp
 *
 * [4] Median of Two Sorted Arrays
 */

#include <iostream>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
    {
        if (nums1.size() > nums2.size()) {
            nums1.swap(nums2);
        }
        auto total_num = nums1.size() + nums2.size();
        auto half_num = total_num / 2;
        size_t min_m1 = 0, max_m1 = nums1.size();

        size_t m1, m2;

        while (true) {
            m1 = (min_m1 + max_m1) / 2;
            m2 = half_num - m1;

            if (m1 < nums1.size() && nums1[m1] < nums2[m2 - 1]) // m1 is too small
            {
                min_m1 = m1 + 1;
                continue;
            }
            if (m1 > 0 && nums1[m1 - 1] > nums2[m2]) // m1 is too big
            {
                max_m1 = m1 - 1;
                continue;
            }
            break;
        };

        int min_of_right;
        if (m1 < nums1.size() && m2 < nums2.size())
            min_of_right = min(nums1[m1], nums2[m2]);
        else if (m1 < nums1.size())
            min_of_right = nums1[m1];
        else if (m2 < nums2.size())
            min_of_right = nums2[m2];

        if (total_num % 2 == 1)
            return min_of_right;

        int max_of_left;
        if (m2 != 0 && m1 != 0)
            max_of_left = max(nums1[m1 - 1], nums2[m2 - 1]);
        else if (m1 != 0)
            max_of_left = nums1[m1 - 1];
        else if (m2 != 0)
            max_of_left = nums2[m2 - 1];

        return (max_of_left + min_of_right) / 2.0f;
    }
};
// @lc code=end

int main()
{
    vector<int> a = { 1, 3 };
    vector<int> b = { 2 };
    Solution s;
    auto r = s.findMedianSortedArrays(b, a);

    cout << "result: " << r << endl;
    return 0;
};
