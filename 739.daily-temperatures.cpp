/*
 * @lc app=leetcode id=739 lang=cpp
 *
 * [739] Daily Temperatures
 */

// @lc code=start
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T)
    {
        auto future_temp = vector<int>(101, -1);

        for (int i = T.size() - 1; i >= 0; i--) {
            auto t = T[i];

            int next_warm_i = (int)T.size();
            for (size_t i2 = t + 1; i2 < future_temp.size(); i2++) {
                if (future_temp[i2] != -1)
                    next_warm_i = min(next_warm_i, future_temp[i2]);
            }
            if (next_warm_i != (int)T.size())
                T[i] = next_warm_i - i;
            else
                T[i] = 0;
            future_temp[t] = i;
        }
        return T;
    }
};
// @lc code=end
