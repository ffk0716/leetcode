#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if x and y and int(matrix[y][x]):
                    lu = matrix[y - 1][x - 1]
                    u = matrix[y - 1][x]
                    l = matrix[y][x - 1]
                    matrix[y][x] = 1 + min(int(u), int(l), int(lu))
                m = max(int(matrix[y][x]), m)
        return m**2


# @lc code=end
