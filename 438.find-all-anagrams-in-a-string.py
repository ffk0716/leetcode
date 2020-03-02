#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#


# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pc = collections.Counter(p)
        ans = []
        if len(s) <= len(p):
            return ans
        sc = collections.Counter(s[:len(p)])
        if sc == pc:
            ans.append(0)
        for i in range(len(p), len(s)):
            sc[s[i]] += 1
            old_char = s[i - len(p)]
            if sc[old_char] == 1:
                del sc[old_char]
            else:
                sc[old_char] -= 1
            if sc == pc:
                ans.append(i - len(p) + 1)
        return ans


# @lc code=end
