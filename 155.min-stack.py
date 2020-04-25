#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#


# @lc code=start
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.sm = []

    def push(self, x: int) -> None:
        self.s.append(x)
        if self.sm:
            self.sm.append(min(self.sm[-1], x))
        else:
            self.sm.append(x)

    def pop(self) -> None:
        if not self.s:
            return None
        self.sm.pop()
        return self.s.pop()

    def top(self) -> int:
        if not self.s:
            return None
        return self.s[-1]

    def getMin(self) -> int:
        return self.sm[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
