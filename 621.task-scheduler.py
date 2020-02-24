#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#


# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        jobs = {}
        for j in tasks:
            if j in jobs:
                jobs[j]+= 1
            else:
                jobs[j] = 1
        print(jobs) 

        it = 0
        cur_n = 0
        while len(jobs):
            it += cur_n
            cur_n = n + 1
            for k,v  in sorted(jobs.items(), key=lambda d: d[1], reverse=True):
                if cur_n == 0:
                    break
                cur_n -= 1
                it += 1
                jobs[k] -= 1
                if jobs[k] == 0:
                    del jobs[k]
                print(k, v)
        return it


# @lc code=end
