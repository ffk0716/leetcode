#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#


# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append(i * i)
            i += 1
        cnt = 0
        pending = {n}
        while pending:
            cnt += 1
            pending2 = set()
            for p in pending:
                for l in lst:
                    if p == l:
                        return cnt
                    if p < l:
                        break
                    pending2.add(p - l)
            pending = pending2


# @lc code=end
