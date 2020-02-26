#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#


# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        ans = []
        for i in range(len(s) - len(p) + 1):
            ss = s[i:i + len(p)]
            ss = sorted(ss)
            if ss == p:
                ans.append(i)
        return ans


# @lc code=end
