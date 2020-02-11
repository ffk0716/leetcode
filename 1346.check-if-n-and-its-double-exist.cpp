/*
 * @lc app=leetcode id=1346 lang=cpp
 *
 * [1346] Check If N and Its Double Exist
 */

// @lc code=start
class Solution {
public:
    bool checkIfExist(vector<int>& arr)
    {
        unordered_set<int> found;
        for (auto i : arr) {
            if (found.count(i * 2))
                return true;
            if (i % 2 == 0 && found.count(i / 2))
                return true;
            found.insert(i);
        }
        return false;
    }
};
// @lc code=end
