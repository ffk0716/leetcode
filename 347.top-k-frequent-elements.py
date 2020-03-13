#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
import collections

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = collections.Counter(nums)
        d = {}
        for v in l:
            c = l[v]
            if c in d:
                d[c].append(v)
            else:
                d[c] = [v]
        ans = []
        for c in reversed(sorted(d)):
            ans += d[c]
            if len(ans) >= k:
                return ans

        ans = [v[0] for v in l.most_common(k)] 
        return ans
        
# @lc code=end

s = Solution()
a = s.topKFrequent([1, 2, 3], 4)
