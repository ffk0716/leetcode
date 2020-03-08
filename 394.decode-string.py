#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#


# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        return self.parse(s)

    def parse(self, s: str) -> str:
        cur_str = ''
        cur_num = ''
        while self.i < len(s):
            c = s[self.i]
            self.i += 1
            if c == '[':
                cur_str += self.parse(s) * int(cur_num)
                cur_num = ''
            elif c == ']':
                return cur_str
            elif c.isdigit():
                cur_num += c
            else:
                cur_str += c
        return cur_str


# @lc code=end

s = Solution()
a = s.decodeString('2[a]')
print(a)
