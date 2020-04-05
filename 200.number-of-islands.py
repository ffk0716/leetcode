#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        def dfs_mark(x, y):
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
                return
            if grid[y][x] != '1':
                return
            grid[y][x] = '0'
            dfs_mark(x + 1, y)
            dfs_mark(x, y + 1)
            dfs_mark(x - 1, y)
            dfs_mark(x, y - 1)

        c = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '1':
                    dfs_mark(x, y)
                    c += 1
        return c


# @lc code=end
