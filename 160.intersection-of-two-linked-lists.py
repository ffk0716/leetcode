#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        a = headA
        b = headB
        if a == None or b == None:
            return None
        while True:
            if a is b:
                return a
            if a == None:
                a = headB
            if b == None:
                b = headA
            if a is b:
                return a
            a = a.next
            b = b.next


# @lc code=end
