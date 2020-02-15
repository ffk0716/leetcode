#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#


# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        r = 0
        for i in range(len(s)):
            # odd
            size = min(i, len(s) - i - 1)
            for i2 in range(size + 1):
                if s[i - i2] == s[i + i2]:
                    r += 1
                else:
                    break
            # even
            size = min(i + 1, len(s) - i - 1)
            for i2 in range(size):
                if s[i - i2] == s[i + 1 + i2]:
                    r += 1
                else:
                    break

        return r


# @lc code=end
