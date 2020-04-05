#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#


# @lc code=start
class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        g = collections.defaultdict(list)
        for c, p in prerequisites:
            g[c].append(p)
        v = [0 for _ in range(numCourses)]

        def dfs(i):
            if v[i] == -1:
                return False
            if v[i] == 1:
                return True
            v[i] = -1
            for p in g[i]:
                if not dfs(p):
                    return False
            v[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# @lc code=end
