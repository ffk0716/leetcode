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
        map<int, size_t> pending;
        int pre = -1;
        for (size_t i = 0; i < T.size(); i++) {
            auto t = T[i];

            vector<int> found;
            for (auto p : pending)
                if (p.first < t)
                    found.push_back(p.first);
            for (auto f : found) {
                size_t i2 = pending[f];
                while (true) {
                    auto next_i = T[i2];
                    T[i2] = i - i2;
                    if (next_i == -1)
                        break;
                    i2 = next_i;
                }
                pending.erase(f);
            }
            if (pending.count(t))
                T[i] = pending[t];
            else
                T[i] = -1;
            pending[t] = i;
        }
        for (auto p : pending) {
            auto i2 = p.second;
            while (true) {
                auto next_i = T[i2];
                T[i2] = 0;
                if (next_i == -1)
                    break;
                i2 = next_i;
            }
        }
        return T;
    }
};
// @lc code=end
