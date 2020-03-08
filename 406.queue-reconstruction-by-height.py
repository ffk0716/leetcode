#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
from typing import List
# @lc code=start
from functools import cmp_to_key


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        people_s = sorted(people, key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people_s:
            ans.insert(p[1], p)
        return ans


# @lc code=end

s = Solution()
ans = s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
print(ans)
